FROM docker.elastic.co/elasticsearch/elasticsearch:7.3.0


COPY elasticsearch-turkish-analysis-1.1-SNAPSHOT.zip /usr/share/elasticsearch-turkish-analysis-1.1-SNAPSHOT.zip
RUN bash -c "yes | ./bin/elasticsearch-plugin install file:///usr/share/elasticsearch-turkish-analysis-1.1-SNAPSHOT.zip"
COPY abbreviations.txt /usr/share/elasticsearch/plugins/elasticsearch-turkish-analysis/tokenization/abbreviations.txt
