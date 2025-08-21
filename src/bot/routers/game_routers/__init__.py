from .statistics_router import router as StatisticsRouter
from .upgrade_router import router as UpgradeRouter

all = [
    StatisticsRouter,
    UpgradeRouter
]