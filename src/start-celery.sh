celery -A researchhub worker -B -Q default,caches,hot_score,elastic_search,external_reporting,notifications,paper_misc,cermine,twitter,pull_papers,logs,purchases,contributions,author_claim -l info --concurrency=1 --prefetch-multiplier=1 -P prefork
