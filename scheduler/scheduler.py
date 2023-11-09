from apscheduler.schedulers.background import BackgroundScheduler
import bot.handlers as handlers

scheduler = BackgroundScheduler()

def start_scheduler():
    """Starts the scheduler with defined jobs."""
    # TODO expand scheduling for different activities
    # Example: Scheduling a job to check validator status every hour
    scheduler.add_job(handlers.check_validators_status, 'interval', hours=1)
    scheduler.start()

def stop_scheduler():
    """Stops the scheduler."""
    scheduler.shutdown()
