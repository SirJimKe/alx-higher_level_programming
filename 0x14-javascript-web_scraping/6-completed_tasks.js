#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error.message);
  } else {
    try {
      const tasksData = JSON.parse(body);
      const completedTasksByUser = {};

      tasksData.forEach(task => {
        if (task.completed) {
          if (!completedTasksByUser[task.userId]) {
            completedTasksByUser[task.userId] = 1;
          } else {
            completedTasksByUser[task.userId]++;
          }
        }
      });

      console.log(completedTasksByUser);
    } catch (parseError) {
      console.error(parseError.message);
    }
  }
});
