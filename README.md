python_network_programing_study
===============================
now under construction...

<pre>
  00_sample_server.py - server program
  01_sample_client.py - client program
  02_easy_client.py   - client program using easy_tcp

  10_pypcap_sample.py - pcap file handling sample
</pre>


tcp client sample
===============================
00_sample_server.py
-------------------------------
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

pcap file handling sample
==============================
10_pypcap_sample.py
------------------------------
<pre>
  $ ./10_pypcap_sample.py
  usage : ./10_pypcap_sample.py pcap_file port check_string
  
  $ ./10_pypcap_sample.py dc20-ctf-0566.pcap 24359 rflr
  ======== 2012-07-29 06:49:24 ========
  'Adventure Farm\x00k\xc84\'\x80\x83\x9f\xc8\xdal0\tHI\x86\xb5\xfc\\"P\xf8L\xa5\x00\\\x99\xb4 \xb9\x95\xaab\x8e\xdfH\x8c\xb6\xb8\xea\xe7\xc3\xc37b\xb4O\xbbe\x08#\xbd\x99\x0c/yr\xbb\x1e\xbf\xcbz\x93\xc9W$\x94\xb8\tA\x89[\x0c(1\xf6\x89\xe3j\x10TSV\xff\x04$j\x1fXP\xcd\x80\x8dd$\x04\x85\xc0u\xef\x8b\x14$1\xdbS\xeb\x16j\x05XS\xcd\x80SSSSSRPf\xb8\x89\x01P\xcd\x80\x0f\x0b\xe8\xe5\xff\xff\xff./key\x00\n'
  ======== 2012-07-29 06:49:25 ========
  'Adventure Farm\x00\x1eB\x80\x1d\x95Nf\xed\xe4\xca\x17\xa1\xc2\x86o~\xb4FMrxu\x16\xcdX6\x07\xac)77\x02\x9e\xd2\xf2?\xc1W\x87N]\x19WX\xbc\x1fY6\x01\x82a\x9f\xaa\xd8\xdb8"\x15\xbc\x9d\x92\xc5\x14\xb0\x89\x13\xf1r\xdd\x89[\x0c(1\xf6\x89\xe3j\x10TSV\xff\x04$j\x1fXP\xcd\x80\x8dd$\x04\x85\xc0u\xef\x8b\x14$1\xdbS\xeb\x16j\x05XS\xcd\x80SSSSSRPf\xb8\x89\x01P\xcd\x80\x0f\x0b\xe8\xe5\xff\xff\xff./key\x00\n'
          .
          .
          .
</pre>
