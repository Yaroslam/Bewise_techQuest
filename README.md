# Bewise_techQuest
  POST {"questions_num": 10}
  built - docker build -t new-app .
  start - docker run -d --restart=always -e DIRECTORY='/tmp/test' -v /tmp/:/tmp/ new-app
