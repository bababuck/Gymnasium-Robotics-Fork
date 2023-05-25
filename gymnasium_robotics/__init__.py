# noqa: D104
from gymnasium.envs.registration import register

from gymnasium_robotics.core import GoalEnv

def register_robotics_envs():
    """Register all environment ID's to Gymnasium."""

    def _merge(a, b):
        a.update(b)
        return a

    for reward_type in ["sparse", "dense"]:
        suffix = "Dense" if reward_type == "dense" else ""
        kwargs = {
            "reward_type": reward_type,
        }

        # Fetch
        register(
            id=f"FetchPickAndPlace{suffix}-v1",
            entry_point="gymnasium_robotics.envs.fetch.pick_and_place:MujocoPyFetchPickAndPlaceEnv",
            kwargs=kwargs,
            max_episode_steps=50,
        )

        register(
            id=f"FetchPickAndPlace{suffix}-v2",
            entry_point="gymnasium_robotics.envs.fetch.pick_and_place:MujocoFetchPickAndPlaceEnv",
            kwargs=kwargs,
            max_episode_steps=50,
        )

__version__ = "1.2.2"


try:
    import sys

    from farama_notifications import notifications

    if (
        "gymnasium_robotics" in notifications
        and __version__ in notifications["gymnasium_robotics"]
    ):
        print(notifications["gymnasium_robotics"][__version__], file=sys.stderr)
except Exception:  # nosec
    pass
