FROM adoptopenjdk/openjdk11:debianslim-jre

ENV FC_LANG en-US LC_CTYPE en_US.UTF-8

# dependencies
RUN apt-get update -yq && apt-get install -yq bash ttf-dejavu fontconfig curl && \
    apt-get clean && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/ && \
    mkdir -p /plugins && chmod a+rwx /plugins && \
    useradd --shell /bin/bash metabase

USER metabase
WORKDIR /app

# copy app from the official image
COPY --from=metabase/metabase:latest /app /app

# expose our default runtime port
EXPOSE 3000

# run it
ENTRYPOINT ["/app/run_metabase.sh"]