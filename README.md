# Software Requirements Specification for the TODO List API

## Project Overview

 The TODO List API is a RESTful API that allows users to create, read, update, and delete TODO lists and TODO items.

## Purpose

 This is a project for the Software Engineering course. The purpose of this project is to demonstrate the use of the Agile software development methodology.

## Scope

This a simple TODO list API that allows users to create, read, update, and delete TODO lists and TODO items. The API is RESTful and uses JSON for data transfer.

## Features

- Create a task
- Delete a task
- Update a task
- Mark a task as complete
- View all tasks
- View a single task
- View completed tasks
- View incomplete tasks

## Database Schema

The database schema for the TODO List API is as follows:

|Field|Type|Description|
|-----|----|-----------|
|id|integer|The unique identifier for the task|
|task|text|The task description|
|description|text|The task description|
|completed|boolean|Whether the task is completed or not|
|created_at|datetime|The date and time the task was created|
|updated_at|datetime|The date and time the task was last updated|

## API Endpoints

The API endpoints for the TODO List API are as follows:

|Method|Endpoint|Description|
|------|--------|-----------|
|GET|/api/tasks|Get all tasks|
|GET|/api/tasks/{id}|Get a single task|
|POST|/api/tasks|Create a new task|
|POST|/api/tasks/{id}|Update a task|
|POST|/api/tasks/{id}/complete|Mark a task as complete|
|POST|/api/tasks/{id}/delete|Delete a task|
|GET|/api/tasks/completed|Get all completed tasks|
|GET|/api/tasks/incomplete|Get all incomplete tasks|

## API Documentation

### Get All Tasks

#### Request

`GET /api/tasks`

    curl -i -H 'Accept: application/json' http://localhost:8000/api/tasks

#### Response

    HTTP/1.1 200 OK
    Date: Mon, 01 May 2017 18:28:00 GMT
    Server: Apache/2.4.18 (Ubuntu)
    X-Powered-By: PHP/7.0.15-0ubuntu0.16.04.4
    Cache-Control: no-cache, private
    Content-Type: application/json

    [
        {
            "id": 1,
            "task": "Task 1",
            "description": "Task 1 description",
            "completed": false,
            "created_at": "2017-05-01 18:28:00",
            "updated_at": "2017-05-01 18:28:00"
        },
        {
            "id": 2,
            "task": "Task 2",
            "description": "Task 2 description",
            "completed": false,
            "created_at": "2017-05-01 18:28:00",
            "updated_at": "2017-05-01 18:28:00"
        }
    ]
