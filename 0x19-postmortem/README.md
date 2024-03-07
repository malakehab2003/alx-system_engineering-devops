                                                        Postmortem

I am really excited to share a story of a failure and solve the error and here is the postmortem this is:

Great thank for ALX for this experience to write about this experience✨
This story was a task in ALX se program and i suppose i experienced this task
Let’s start🤩
Summary of the issue:
The issue occurred between 12:07 to 12:48 our website was down and 100% of our users got 500 as a status code when searching for our website and the cause was fault in extension of a specific file
Timeline:
The issue occurred at 12:07 pm
It detected at 12:12pm 🆘
We start to solve it at 12:15
We found the error at 12:30
Everything was okay at 12:48

The issue detected by complaining of a customer
We started searching for the error in all our servers, source code and database
Everything was correct in database and source code and it was misleading
We asked the project manager to help us
Finally we found the extension error and solved it
The root cause:
The root cause of the error was when we wrote our code we added a file with the extension .php and when we imported this file to our web server and ran everything locally everything seemed to be okay when we uploaded the whole project to the web server here the problem occurred 
To fix the issue we firstly searched the whole source code to check if everything is okay and we tested each part of it and everything was okay then we searched our database to find if the problem generated from it but also everything was okay finally we said that the problem must be from our web server and when we debugged it we found the problem the extension was .phpp instead of php and finally we solved this issue and solved the whole problem🤩
Corrective and preventative measures:
We should add web server monitoring app to monitor if any problem happened in our web server and we should review the work of each other specially in extension errors and handwriting errors
