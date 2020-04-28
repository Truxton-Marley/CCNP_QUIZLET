###CONFIGURATION LEVELS
EXEC = {
    "prompt": "R1#",
    "options": ["show ip interface brief"]
    }

CONFIG = {
    "prompt": "R1(config)#",
    "options": ["crypto"]
    }

CONFIG_ISAKMP = {
    "prompt": "R1(config-isakmp)#",
    "options": ["authentication", "encryption", "group", "hash", "lifetime"]
    }

IPSEC_PROFILE = {
    "prompt": "R1(ipsec-profile)#",
    "options": ["set", "match"]
    }
    
CFG_CRYPTO_TRANS = {
    "prompt": "R1(cfg-crypto-trans)#",
    "options": ["mode transport", "mode tunnel"]
    }

