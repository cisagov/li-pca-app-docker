ARG VERSION=unspecified

FROM python:3.10.1
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

RUN apt-get update && \
 apt-get install wget

WORKDIR ${CISA_HOME}

RUN wget -O sourcecode.tgz https://github.com/cisagov/li-pca-app/archive/v${VERSION}.tar.gz && \
  tar xzf sourcecode.tgz --strip-components=1 && \
  pip3 install -e . && \
  rm sourcecode.tgz

USER cisa

EXPOSE 8080/TCP
VOLUME ["/usr/src/api"]
ENTRYPOINT ["python3"]
CMD ["-m", "api"]
