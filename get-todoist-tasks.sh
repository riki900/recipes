curl -o json/projects.json https://api.todoist.com/sync/v8/sync \
    -d token=7b409adf2e73047fa9665765bafe186626e62519 \
    -d sync_token=* \
    -d resource_types='["projects"]'


curl -o json/tasks.json -X GET \
  https://api.todoist.com/rest/v1/tasks \
  -H "Authorization: Bearer 7b409adf2e73047fa9665765bafe186626e62519"
