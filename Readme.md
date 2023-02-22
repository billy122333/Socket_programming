# Socket Programming practice
## Introdution
傳輸層 中最 廣泛被使用的協定 分為 TCP 及 UDP ，而 不管是內部
協議的運作，還是應用在的層面皆 略有不同。
了解協議的運作及優缺點後，我便實作了兩種不同協議的語音
傳輸方式，雖然知道廣泛被使用在語音傳輸的協定為 UDP ，因語音
對資料傳輸的穩定性較不要求，反而對傳輸速率較為看中，但我仍
想知道 TCP 狀態下的傳輸速率以及 UDP 的差距，以及 UDP 在傳輸
時的穩定性是否較 TCP 來說差距很大，於是便做了這個可以透過兩
種方式進行語音傳輸的程式進行比較。
## What could it do?
- It could simply connect the server and the client with TCP and UDP socket.
### Server
- Get the sound package from the client.
  - play it
  - recored it as a wave. 
### Client
- Get the sound from the hardware and send it to the server.

## Result
- ![image](https://user-images.githubusercontent.com/75492436/220570327-4f11e066-a67b-43b5-9d21-9ee3ed85dc78.png)
- ![image](https://user-images.githubusercontent.com/75492436/220570343-8066775e-1327-4714-bdaf-d7068073461a.png)
