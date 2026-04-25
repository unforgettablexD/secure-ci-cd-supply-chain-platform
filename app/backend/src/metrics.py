from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    "request_count",
    "Total HTTP requests",
    ["method", "path", "status"],
)
REQUEST_LATENCY_SECONDS = Histogram(
    "request_latency_seconds",
    "Request latency",
    ["method", "path"],
)
QUOTE_GENERATED_TOTAL = Counter("quote_generated_total", "Quotes generated")
PAYMENT_SUCCESS_TOTAL = Counter("payment_success_total", "Successful payments")
PAYMENT_FAILURE_TOTAL = Counter("payment_failure_total", "Failed payments")
SEVERITY_EVALUATION_TOTAL = Counter("severity_evaluation_total", "Severity evaluations")
SEVERITY_HIGH_TOTAL = Counter("severity_high_total", "High/critical severity events")
SECURITY_AUDIT_EVENTS_TOTAL = Counter(
    "security_audit_events_total",
    "Security-relevant audit events",
)
