token=""
curl -s -H "X-Team-Token: $token" -X PUT -d '["IRMR2583JSHPV0NX6NL9GE428DB659F="]' http://monitor.ructfe.org/flags | json_pp