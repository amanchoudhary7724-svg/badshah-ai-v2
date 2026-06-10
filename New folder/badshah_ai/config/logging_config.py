import logging
from badshah_ai.config.settings import settings

def setup_logging() -> None:
    settings.prepare_dirs()
    logging.basicConfig(
        filename=str(settings.log_file),
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        encoding="utf-8",
    )
