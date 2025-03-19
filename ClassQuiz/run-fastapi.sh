OTEL_RESOURCE_ATTRIBUTES=service.name=classquiz-rest \
OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:4318" \
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf \
OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED="true" \
OTEL_PYTHON_LOG_CORRELATION="true" \
opentelemetry-instrument --logs_exporter otlp pipenv run uvicorn classquiz:app --proxy-headers