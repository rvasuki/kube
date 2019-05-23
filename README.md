# kubernatis_ingress_stickysession_Scaling


curl -d '{"target":"backend-1", "username":"user one"}' -H "Content-Type: application/json" -X POST <external-ip>:<port>/hit_backend3

curl -d '{"target":"backend-2", "username":"user one"}' -H "Content-Type: application/json" -X POST <external-ip>:<port>/hit_backend3

curl -d '{"target":"backend-3", "username":"user one"}' -H "Content-Type: application/json" -X POST <external-ip>:<port>/hit_backend3
      
 
