
Level: No query string
TTL: One day
```
(starts_with(http.request.full_uri, "https://feed.jimchen.me") or
 starts_with(http.request.full_uri, "https://nezha.jimchen.me") or
 starts_with(http.request.full_uri, "https://grafana.jimchen.me") or
 starts_with(http.request.full_uri, "https://chat.jimchen.me") or
 starts_with(http.request.full_uri, "https://git.jimchen.me") or
 starts_with(http.request.full_uri, "https://link.jimchen.me") or
 starts_with(http.request.full_uri, "https://jimchen.me") or
 starts_with(http.request.full_uri, "https://portainer.jimchen.me") or
 starts_with(http.request.full_uri, "https://matrix.jimchen.me") or
 starts_with(http.request.full_uri, "https://peertube.jimchen.me") or
 starts_with(http.request.full_uri, "https://mastodon.jimchen.me") or
 starts_with(http.request.full_uri, "https://cdn.jimchen.me") or
 starts_with(http.request.full_uri, "https://bucket.jimchen.me"))
```