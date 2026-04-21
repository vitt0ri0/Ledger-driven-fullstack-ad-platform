from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, FrozenSet, Iterable, Optional, Set


class InvalidTransitionError(ValueError):
    """Raised when an event is not allowed from the current state."""


@dataclass(frozen=True)
class Transition:
    event: str
    source: str
    target: str


# A couple of ready-to-use workflow transition sets for MVP flows.
RESERVATION_TRANSITIONS: tuple[Transition, ...] = (
    Transition("activate", "draft", "active"),
    Transition("consume", "active", "consumed"),
    Transition("release", "active", "released"),
)

PAYMENT_TRANSITIONS: tuple[Transition, ...] = (
    Transition("mark_pending", "created", "pending"),
    Transition("mark_succeeded", "pending", "succeeded"),
    Transition("mark_failed", "pending", "failed"),
)


class StateMachine:
    """
    Lightweight FSM core for explicit workflow transitions.

    Example:
        sm = StateMachine(
            initial_state="created",
            transitions=[
                Transition("activate", "created", "active"),
                Transition("finish", "active", "completed"),
            ],
            terminal_states={"completed"},
        )

        sm.apply("activate")
        sm.apply("finish")
    """

    def __init__(
        self,
        *,
        initial_state: str,
        transitions: Iterable[Transition],
        terminal_states: Optional[Iterable[str]] = None,
    ) -> None:
        self._current_state = initial_state
        self._terminal_states: FrozenSet[str] = frozenset(terminal_states or [])
        self._transitions_by_state: Dict[str, Dict[str, str]] = {}
        self._known_states: Set[str] = {initial_state, *self._terminal_states}

        for transition in transitions:
            self._known_states.add(transition.source)
            self._known_states.add(transition.target)
            state_events = self._transitions_by_state.setdefault(transition.source, {})
            if transition.event in state_events:
                raise ValueError(
                    f"Duplicate transition for source='{transition.source}' "
                    f"and event='{transition.event}'."
                )
            state_events[transition.event] = transition.target

    @property
    def current_state(self) -> str:
        return self._current_state

    @property
    def is_terminal(self) -> bool:
        return self._current_state in self._terminal_states

    def allowed_events(self) -> FrozenSet[str]:
        events = self._transitions_by_state.get(self._current_state, {})
        return frozenset(events.keys())

    def can_apply(self, event: str) -> bool:
        return event in self.allowed_events()

    def apply(self, event: str) -> str:
        if self.is_terminal:
            raise InvalidTransitionError(
                f"State '{self._current_state}' is terminal; event '{event}' is not allowed."
            )

        next_state = self._transitions_by_state.get(self._current_state, {}).get(event)
        if next_state is None:
            allowed = ", ".join(sorted(self.allowed_events())) or "none"
            raise InvalidTransitionError(
                f"Invalid event '{event}' from state '{self._current_state}'. "
                f"Allowed events: {allowed}."
            )

        self._current_state = next_state
        return self._current_state


def build_reservation_fsm(initial_state: str = "draft") -> StateMachine:
    return StateMachine(
        initial_state=initial_state,
        transitions=RESERVATION_TRANSITIONS,
        terminal_states={"consumed", "released"},
    )


def build_payment_fsm(initial_state: str = "created") -> StateMachine:
    return StateMachine(
        initial_state=initial_state,
        transitions=PAYMENT_TRANSITIONS,
        terminal_states={"succeeded", "failed"},
    )

