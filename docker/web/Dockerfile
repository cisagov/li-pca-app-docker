ARG VERSION=unspecified

FROM node:12.18.3

ARG VERSION

# For a list of pre-defined annotation keys and value types see:
# https://github.com/opencontainers/image-spec/blob/master/annotations.md
# Note: Additional labels are added by the build workflow.
LABEL org.opencontainers.image.authors="mark.feldhousen@cisa.dhs.gov"
LABEL org.opencontainers.image.vendor="Cybersecurity and Infrastructure Security Agency"

ARG CISA_UID=421
ENV CISA_HOME="/home/cisa"

RUN addgroup --system --gid ${CISA_UID} cisa \
  && adduser --system --uid ${CISA_UID} --ingroup cisa cisa

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    wget \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# WORKDIR ${CISA_HOME}/src/ui
# WORKDIR /usr/src/ui
# RUN pwd && ls -a

WORKDIR ${CISA_HOME}

RUN wget -O sourcecode.tgz https://github.com/cisagov/li-pca-app/archive/refs/tags/v0.0.1-rc4.tar.gz && \
  tar xzf sourcecode.tgz --strip-components=3 && \
  npm ci && \
  rm sourcecode.tgz

# USER cisa

# EXPOSE 3000/TCP
# COPY . /usr/src/ui
# COPY . $CISA_HOME
# WORKDIR /usr/src/ui
# RUN cd $CISA_HOME/src/ui && npm ci

# COPY . $CISA_HOME

# WORKDIR ${CISA_HOME}
# COPY . .
#
# WORKDIR /usr/src/ui
# WORKDIR /usr/src/ui/src/ui
# COPY ./src  .
# WORKDIR ./src/ui
# RUN cd ./src/ui && npm install
# RUN npm install
# RUN cd ./src/ui && npm install

USER cisa
# EXPOSE 3000
EXPOSE 3000/TCP
VOLUME ["/usr/src/ui"]
ENTRYPOINT [ "npm", "start" ]
