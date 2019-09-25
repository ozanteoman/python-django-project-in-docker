#!/usr/bin/env bash

# TODO do not forget add elasticsearch-turkish-analysis-1.0-SNAPSHOT.zip and abbreviations.txt in project path before use this

docker exec -it docker_elasticsearch_1 bash -c "yes | ./bin/elasticsearch-plugin remove elasticsearch-turkish-analysis"

docker exec docker_elasticsearch_1 rm -f /usr/share/elasticsearch-turkish-analysis-1.1-SNAPSHOT.zip

docker exec docker_elasticsearch_1 rm -f /usr/share/elasticsearch/plugins/elasticsearch-turkish-analysis

docker cp elasticsearch-turkish-analysis-1.1-SNAPSHOT.zip docker_elasticsearch_1:/usr/share/elasticsearch-turkish-analysis-1.1-SNAPSHOT.zip

docker exec -it docker_elasticsearch_1 bash -c "yes | ./bin/elasticsearch-plugin install file:///usr/share/elasticsearch-turkish-analysis-1.1-SNAPSHOT.zip"

docker cp abbreviations.txt docker_elasticsearch_1:/usr/share/elasticsearch/plugins/elasticsearch-turkish-analysis/tokenization/abbreviations.txt

docker restart docker_elasticsearch_1
