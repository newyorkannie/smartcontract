{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from xrpl.clients import JsonRpcClient\
from xrpl.ledger import get_fee\
from xrpl.models.transactions import EscrowCreate, Payment\
\
client = JsonRpcClient('https://s.altnet.rippletest.net:51234')  # Use testnet for testing\
\
sender_address = "your_sender_address"\
receiver_address = "your_receiver_address"\
\
# Create an escrow\
escrow_transaction = EscrowCreate(\
    account=sender_address,\
    destination=receiver_address,\
    amount="1000000",  # Amount in drops (1 XRP = 1,000,000 drops)\
    condition="your_condition",\
    cancel_after=123456789,  # Block number after which the sender can cancel\
    finish_after=123456788   # Block number after which the receiver can claim\
)\
\
# Sign and submit the escrow transaction\
escrow_transaction.sign("your_private_key")\
response = client.submit(escrow_transaction)\
print(response)\
}