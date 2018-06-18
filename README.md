# worldcup2018-tickets
I created these scripts to help me to buy tickets in the WorldCup 2018 in last call for the next day match
I didn't have time to automate everything as I have done in 2014. 
So I needed to enter the capthas and configure the snippets manually

1. The index.js file is just a tutorial to run in the console browser and not a real js file

2 .The python file is a AWS Lambda function to send email notifications when you have tickets available for oyur wished match

You need to add permission to run SES in the IAM role for this function
Apart from that create an event in CloudWatch to trigger this function every minute to verify availability
Change the email_from = 'xxxx', email_to = 'xxxxx' in the code and verify them in the SES
The default daily limit of SES is 200 emails/day. So you have to ask AWS to increase this quota.
