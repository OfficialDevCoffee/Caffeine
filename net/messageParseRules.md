### Caffeine Chatting Server Message Parsing Rules
 **dev. Coffee**에서 개발하는 **Caffeine**은 클라이언트 측에서 보낸 내용을 파싱하기 위하여, 메시지를 전달할 때 일련의 절차를 이용하여 전달하도록 하고 있습니다.

#### Message Structure
 모든 메시지는 Python Dictonary의 형태로 구조화되어 JSON의 형태로 문자열로 전송합니다. 모든 데이터 전송은 다음의 Dict 형태로 구조화되어 이루어집니다.

##### Basic Message Structure
 파일 전송이나, 귓속말, 이모지 등을 비롯하고도 일반적인 평문의 전송의 경우는 데이터가 기본적으로는 다음의 정보를 포함하는 딕셔너리로 전달됩니다.
 > Status, Sender_Address, Message
 ###### Status
  이 정보를 송신하는 모드를 지시합니다. 일반적으로 평문 전달의 경우는 'Text'와 같은 값을 가지고, 귓속말의 경우는 'Whisper', 파일의 경우는 'File', 이모지의 경우는 'Emoji', 입/퇴장과 같은 채팅방 관련 이벤트의 경우는 'Event'의 값을 가집니다.
 ###### Sender_Address
  이 정보를 송신한 클라이언트의 ipv4 주소를 담아 전달합니다.
 ###### Message
  이 부분에 실제 평문을 넣어 전달합니다.

##### Whispering Message Structure
 귓속말 메시지의 경우 다음의 구조를 가지게 됩니다.
 > Status, Sender_Address, Reciever_Address, Message
 ###### Status
  이 정보가 귓속말임을 'Whisper'라는 값으로 명시합니다.
 ###### Sender_Address
  이 정보를 송신한 클라이언트의 ip4v 주소를 담아 전달합니다.
 ###### Reciever_Address
  이 정보를 수신해야 하는 클라이언트의 ipv4 주소를 담아 전달합니다.
 ###### Message
  실제 유저가 입력한 귓속말을 전달합니다.

##### Event Message Structure
 채팅방에 유저가 입장/퇴장하거나, 서버와 클라이언트 간의 정보 송/수신, 또는 서버 측 공지 등과 같은 이벤트성 혹은 관리성 메시지의 경우는 Event Message로 전송됩니다. Event Message는 일반적으로 다음의 구조를 가지게 됩니다.
 > Status, Sender_Address, Event_Type, Data
 ###### Status
  이 정보가 이벤트성 혹은 관리성임을 'Event'라는 값으로 명시합니다.
 ###### Sender_Address
  이 정보를 송신한 클라이언트의 ipv4 주소를 담아 전달합니다. 서버의 경우는 예외적으로, 'server'라는 문자열 값을 가집니다.
 ###### Event_Type & Data
  **Event_Type** 부분에는 이벤트의 종류를 담아 전달합니다. **Caffeine**에서 발생 가능한 이벤트에는 다음의 종류들이 있으며, 그 각각에서 전송하는 **Data**는 다음의 각 세부와 같이 JSON화된 객체로 전송됩니다. 데이터 전송의 효율성을 위하여 전송되는 Event_Type는 다음 각 항목에서 3자의 약자를 전송합니다.
  1. Log In Request - LIR
   이 종류의 Event Type는 새 사용자가 채팅방에 입장할 때, 클라이언트 측에서 서버에 자신의 정보를 담아 발송합니다. 서버는 Log In Request Event를 수신하였을 경우, 자신의 유저 리스트를 업데이트하고, 이를 전 클라이언트에 브로드캐스트합니다. 이 때, 서버 측에서는 전 유저에게 User List Event를 송신합니다. 이 경우 **Data**는 *Username, Password*만으로 구성됩니다.
  2. User List - URL
   이 종류의 Event Type는 유저 리스트의 변동이 있거나, 최초로 채팅방에 입장한 유저에게 현재 채팅방에 있는 유저와 그 주소를 전달할 때 서버에서 발송됩니다. 클라이언트는 User List Event를 수신하였을 경우, 자신의 유저 리스트를 서버에서 발송한 데이터와 동일하게 업데이트합니다. 이 경우 **Data**는 *Username*의 키에 대하여 *Address* 값을 가지는 JSON 객체로 전송됩니다.
  3. Name Change Request - NCR
   이 종류의 Event Type는 사용자가 자신의 별명을 변경할 때, 클라이언트 측에서 서버에 자신의 정보를 담아 발송합니다. 서버는 Name Change Request Event를 수신하였을 경우, 자신의 유저 리스트에 변경된 정보를 업데이트하고, 이를 전 클라이언트에 브로드캐스트합니다. 이 때, 서버 측에서는 전 유저에게 User List Event를 송신합니다. 이 경우 **Data**는 *Changed_Username*만으로 구성됩니다.
  4. Log Out Request - LOR
   이 종류의 Event Type는 사용자가 채팅방에서 나갈 때, 클라이언트 측에서 서버에 자신의 정보를 담아 발송합니다. 서버는 Log Out Request Event를 수신하였을 경우, 자신의 유저 리스트를 업데이트하고, 이를 전 클라이언트에 브로드캐스트합니다. 이 때, 서버 측에서는 전 유저에게 User List Event를 송신합니다. 이 경우 **Data**에는 아무 것도 포함되지 않습니다.
  5. File Upload Request - FUR
   이 종류의 Event Type는 클라이언트 측에서 파일 업로드를 요청하는 경우 서버에 자신의 정보를 담아 발송합니다. 서버는 File Upload Request Event를 수신하였을 경우, 새로운 쓰레드와 소켓을 선언하여 파일을 서버 측으로 옮겨 받습니다. 이 때 File Transmission Start Event, File Transmission Event, File Transmission End Event, File Transmission Cancel Event 등이 발생합니다. (회선 블록킹 방지) 이후, 파일이 준비되었을 경우, 전 클라이언트에 File Ready Event를 송신합니다. 이 경우 **Data**는 *Filename, Filesize*로 구성됩니다.
  6. File Ready - FRD
   이 종류의 Event Type는 서버 측에서 클라이언트의 파일이 준비되었을 경우, 전 클라이언트에 파일이 준비되었다고 알릴 때 송신됩니다. 클라이언트가 이를 수신하였을 경우, 파일을 송신한 클라이언트는 업로드가 완료되었다는 메시지를 표시하며, 그 이외의 클라이언트는 파일명과 보낸 이가 명시된 파일 다운로드 메시지를 표시합니다. 클라이언트에 표시된 파일 다운로드 메시지를 유저가 클릭하는 경우, 이 클라이언트는 서버에 File Download Request Event를 송신합니다. 이 경우 **Data**는 *Filenumber, Filename, File_Sender, Filesize*로 구성됩니다.
  7. File Download Request Event - FDR
   이 종류의 Event Type는 클라이언트 측에서 파일 다운로드를 요청하는 경우 서버에 자신의 정보를 담아 발송합니다. 서버는 File Download Request Event를 수신하였을 경우, 새로운 쓰레드와 소켓을 선언하여 파일을 클라이언트 측으로 전송합니다. 이 때도 마찬가지로 File Transmission Start Event, File Transmission Event, File Transmission End Event, File Transmission Cancel Event 등이 발생합니다. (회선 블록킹 방지) 이 경우 **Data**는 *Filenumber*만을 포함합니다.
  8. File Transmission Start Event - FTS
   이 종류의 Event Type는 서버, 혹은 클라이언트 측에서 파일을 지금부터 보내겠다고 하는 경우, 상대 측의 파일 전용 소켓으로 송신됩니다. 상대측은 이 이벤트를 수신하는 경우 파일 전용 소켓에 대해서 전달된 파일명으로 파일을 저장하기 시작합니다. 이 경우 **Data**에는 아무것도 포함되지 않습니다.
  9. File Transmission Event - FTM
   이 종류의 Event Type는 서버, 혹은 클라이언트 측에서 파일 정보를 송신하는 경우 지정됩니다. 상대측은 이 이벤트를 수신하는 경우 파일 전용 소켓으로 파일 정보를 기록합니다. 이 경우 **Data**는 예외적으로 JSON 객체가 아니며, 파일 정보를 담은 Byte로 구성됩니다.
  10. File Transmission End Event - FTE
   이 종류의 Event Type는 서버, 혹은 클라이언트 측에서 파일 전송이 종료된 경우, 상대 측의 파일 전용 소켓으로 송신됩니다. 상대측은 이 이벤트를 수신하는 경우 파일을 저장하고 닫습니다. 이 경우 **Data**에는 아무것도 포함되지 않습니다.
  11. File Transmission Cancel Event - FTC
   이 종류의 Event Type는 서버, 혹은 클라이언트 측에서 파일 전송이 중도에 취소되는 경우, 상대 측의 파일 전용 소켓으로 송신됩니다. 상대측은 이 이벤트를 수신하는 경우 진행 중인 파일 저장을 중지하고, 파일을 삭제합니다. 이 경우 **Data**에는 아무것도 포함되지 않습니다.
  12. Emoji - EMJ
   이 종류의 Event Type는 서버, 혹은 클라이언트 측에서 이모지를 송신하는 경우 발송됩니다. 상대측은 이 이벤트를 수신하는 경우 다음 Emoji 데이터를 이용해 해당 이모지를 표시합니다. 이 경우 **Data**에는 *Emoji_Name*만이 포함됩니다.
  13. Connection Cancel Event - CNC
   이 종류의 Event Type는 서버 측에서 클라이언트 측의 접속을 중지하고 이를 통보하는 경우 발송됩니다. 상대측은 이 이벤트를 수신하는 경우, 강퇴임을 표시하고 서버와의 연결을 끊습니다. 이 경우 **Data**에는 *Reason*만이 포함됩니다.
  14. Notice Event - NTC
   이 종류의 Event Type는 서버 측에서 클라이언트 측으로 공지를 통보하는 경우 발송됩니다. 클라이언트는 이 이벤트를 수신하는 경우, 별도의 형식으로 서버 공지를 화면에 표시합니다. 이 경우 **Data**에는 *Text*만이 포함됩니다.