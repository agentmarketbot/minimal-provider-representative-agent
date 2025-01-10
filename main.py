import multiprocessing
import sys
import time

from loguru import logger

from src.market_scan import market_scan_handler
from src.solve_instances import solve_instances_handler


def run_market_scan():
    while True:
        try:
            logger.info("Starting market scan")
            market_scan_handler()
            logger.info("Market scan completed successfully")
            logger.info("Waiting 10 seconds before next market scan...")
            time.sleep(10)
        except Exception as e:
            logger.error(f"Market scan iteration failed: {str(e)}")
            logger.exception(e)
            time.sleep(30)  # Longer delay on failure


def run_solve_instances():
    while True:
        try:
            logger.info("Starting solve_instances")
            solve_instances_handler()
            logger.info("solve_instances completed successfully")
            logger.info("Waiting 10 seconds before next solve_instances...")
            time.sleep(10)
        except Exception as e:
            logger.error(f"Solve instances iteration failed: {str(e)}")
            logger.exception(e)
            time.sleep(30)  # Longer delay on failure


def main():
    logger.info("Starting application...")

    market_scan_process = multiprocessing.Process(target=run_market_scan)
    solve_instances_process = multiprocessing.Process(target=run_solve_instances)

    market_scan_process.start()
    solve_instances_process.start()

    try:
        market_scan_process.join()
        solve_instances_process.join()
    except KeyboardInterrupt:
        logger.info("Application stopped by user")
        market_scan_process.terminate()
        solve_instances_process.terminate()
        market_scan_process.join()
        solve_instances_process.join()
    except Exception as e:
        logger.info("Fatal error in main loop")
        market_scan_process.terminate()
        solve_instances_process.terminate()
        sys.exit(1)


if __name__ == "__main__":
    main()
