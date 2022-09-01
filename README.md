# Skypia-Verification-bot

A bot made for Skypia SMP used for automatic user verification.

Skypia discord invite:
https://discord.gg/kxmTqsHwZM

If you want to copy the code:
1. Change the channel/role id's on some of the lines 
2. Fix line 23 (and some other lines with config or data feature) so that it says where the following config file is
3. Make a config.json file with the following code:

{

    "TOKEN": "Bot-token-here",
    
    "redpassword": "reddit-account-password-here",
    
    "redsecret": "reddit-secret-here",
    
    "redclientid" : "reddit-client-id-here"
    
    }

(reddit passwords etc. are needed for the +reddit command to work, due to PRAW needing it. You can just make a burner account)
