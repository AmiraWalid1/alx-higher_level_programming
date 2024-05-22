#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const tasks = JSON.parse(body);
  const completedTask = {};
  for (const task of tasks) {
    if (task.completed === true) {
      if (task.userId in completedTask) {
        completedTask[task.userId]++;
      } else {
        completedTask[task.userId] = 1;
      }
    }
  }
  console.log(completedTask);
});
