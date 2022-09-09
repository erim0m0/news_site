# from datetime import timedelta

broker_url = 'redis://localhost:6379'
# result_backend = 'redis://localhost:6379'
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json', 'json']
# result_expires = timedelta(days=1, hours=12)
task_always_eager = False
worker_prefetch_multiplier = 4
