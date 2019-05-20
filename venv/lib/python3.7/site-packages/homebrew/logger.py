import logging
import sys

logger = logging.getLogger()
formatter = logging.Formatter("%(message)s")
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

UNDERLINE_SYMBOL = "-"


def log_title(logline):
    logger.info(logline)
    logger.info(len(logline) * UNDERLINE_SYMBOL)


def log_blank_line():
    logger.info("")


def log(
    installed,
    packages_not_needed_by_other,
    packages_needed_by_other,
    package_dependencies,
):

    log_title("Installed packages:")
    logger.info(", ".join(sorted(installed)))
    log_blank_line()

    log_title("No package depends on these packages:")
    logger.info(", ".join(sorted(packages_not_needed_by_other)))
    log_blank_line()

    log_title("These packages are needed by other packages:")
    for package, needed_by in sorted(packages_needed_by_other.items()):
        logger.info("Package {} is needed by: {}".format(package, ", ".join(needed_by)))
    log_blank_line()

    log_title("These packages depend on other packages:")
    for package, package_dependencies in sorted(package_dependencies.items()):
        logger.info(
            "Package {} depends on: {}".format(package, ", ".join(package_dependencies))
        )
    log_blank_line()
