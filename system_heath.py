import psutil
import logging

# Set thresholds
cpu_threshold = 80
mem_threshold = 80
disk_threshold = 90
proc_threshold = 500

# Set up logging
logging.basicConfig(filename='system_health.log', level=logging.INFO)

# Log start
logging.info("System Health Check Started")

# Check CPU usage
cpu_usage = psutil.cpu_percent()
logging.info(f"CPU usage: {cpu_usage}%")
if cpu_usage > cpu_threshold:
  logging.warning(f"CPU usage exceeded {cpu_threshold}%: {cpu_usage}%")

# Check memory usage
mem_usage = psutil.virtual_memory().percent
logging.info(f"Memory usage: {mem_usage}%")
if mem_usage > mem_threshold:
  logging.warning(f"Memory usage exceeded {mem_threshold}%: {mem_usage}%")

# Check disk space
disk_usage = psutil.disk_usage('/').percent
logging.info(f"Disk usage: {disk_usage}%")
if disk_usage > disk_threshold:
  logging.warning(f"Disk usage exceeded {disk_threshold}%: {disk_usage}%")

# Check running processes
proc_count = len(psutil.pids())
logging.info(f"Number of running processes: {proc_count}")
if proc_count > proc_threshold:
  logging.warning(f"Number of running processes exceeded {proc_threshold}: {proc_count}")

# Log completion
logging.info("System Health Check Complete")

print("System Health Check Complete.")

