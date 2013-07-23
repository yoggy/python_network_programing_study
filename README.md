python_network_programing_study
===============================
now under construction...

<pre>
  00_sample_server.py - server program
  01_sample_client.py - client program
  02_easy_client.py   - client program using easy_tcp
</pre>

00_sample_server.py
===============================
00_sample_server.py start listening on port 12345.
<pre>
  $ ./00_sample_server.py
</pre>

manually connect
------------------------------
<pre>
  $ nc localhost 12345
  +---------------------------------------+
  |                                       |
  |   welcome to sorting problem server   |
  |                                       |
  +---------------------------------------+
  
  please sort numbers into ascending order.
  numbers : 169 119 158
  > 119 158 169
  correct answer!!
  
  please sort numbers into ascending order.
  numbers : 58 121 106 178
  > 58 106 121 178
  correct answer!!
  
  please sort numbers into ascending order.
  numbers : 96 96 171 74 178
  >
        .
        .
        .
</pre>

autopilot program (01_sample_client.py)
------------------------------
<pre>
  $ ./01_sample_client.py
  usage : ./01_sample_client.py host port

  $ ./01_sample_client.py ::1 12345
  +---------------------------------------+
  |                                       |
  |   welcome to sorting problem server   |
  |                                       |
  +---------------------------------------+
  
  please sort numbers into ascending order.
  numbers : 99 90 113
  >
  send : 90 99 113
  correct answer!!
        .
        .
        .
  congraturation!!! key=85fafe70367a388d5df98c4dfa11eac7
  bye bye
</pre>

autopilot program (02_easy_client.py)
------------------------------
<pre>
  $ ./02_easy_client.py
  usage : ./02_easy_client.py host port

  $ ./02_easy_client.py ::1 12345 2>/dev/null
  !!!!!!!! key is 85fafe70367a388d5df98c4dfa11eac7 !!!!!!!!
</pre>

<pre>
  $ ./02_easy_client.py
  usage : ./02_easy_client.py host port
  
  $ ./02_easy_client.py ::1 12345
  easy_tcp[D] connect() : host=::1, port=12345
  easy_tcp[I] connect() : connect() success...host=::1, port=12345
  easy_tcp[D] recv() : size=284, data=+---------------------------------------+
  |                                       |
  |   welcome to sorting problem server   |
  |                                       |
  +---------------------------------------+
  
  please sort numbers into ascending order.
  numbers : 68 176 49
  >
  easy_tcp[D] send() : data=49 68 176
  
  easy_tcp[D] recv() : size=90, data=correct answer!!
  
  please sort numbers into ascending order.
  numbers : 25 8 195 120
  >
  easy_tcp[D] send() : data=8 25 120 195
          .
          .
          .
  easy_tcp[D] recv() : size=85, data=correct answer!!
  
  congraturation!!! key=85fafe70367a388d5df98c4dfa11eac7
  bye bye
  
  !!!!!!!! key is 85fafe70367a388d5df98c4dfa11eac7 !!!!!!!!
  easy_tcp[I] close() : close socket...host=::1, port=12345
</pre>

