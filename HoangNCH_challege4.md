# CÁC VẤN ĐỀ VỀ NETWORK PROGRAMMING VÀ HTTP client

### I. LÝ THUYẾT:

##### 1) Request line của một HTTP request:

Dòng Request Line của mỗi HTTP Request bao gồm 3 thành phần và được cách nhau bởi một khoảng trắng:

- Một **động từ** chỉ HTTP method. Có 8 động từ phổ biến gồm: **GET**, **POST**, **PUT**, **HEAD**, **DELETE**, **CONNECT**,  **OPTIONS**, **TRACE**, **PATCH**. 2 method được sử dụng phổ biến nhất là **GET** và **POST**.
- **Requested URL**: dùng để chỉ định nguồn tài nguyên được yêu cầu, theo sau nó có thể có một chuỗi truy vấn tùy chọn chứa các tham số mà client đang truyền đến tài nguyên đó. Có 2 loại truy vấn trong requested URL: **query parameter** được chỉ định bằng dấu `?`, **path parameter** được chỉ định bằng dấu `/` (như một đường dẫn) trong URL.
- **Phiên bản HTTP** đang được client sử dụng. Các phiên bản HTTP duy nhất được sử dụng phổ biến trên Internet là 1.0 và 1.1 và hầu hết các trình duyệt mặc định sử dụng phiên bản 1.1. Có một số khác biệt giữa các thông số kỹ thật của hai phiên bản, tuy nhiên, sự khác biệt duy nhất có thể gặp phải khi tấn công các ứng dựng web là trong phiên bản 1.1, bắt buộc phải có request header `Host` .
- VD về request line: 
  - Có **path parameter**: `GET /product/1 HTTP/1.1`
  - Có **query parameter**: `GET /product/index.php?id=1&page=2 HTTP/1.1 `

##### 2) Định dạng của một URL:

URL (viết tắt của Uniform Resource Locator) là một định danh duy nhất cho tài nguyên web mà qua đó tài nguyên đó có thể được truy xuất. Định dạng của hầu hết các URL biểu diễn như sau (các thành phần trong dấu ""[]" là không bắt buộc):

​                      `protocol://hostname[:port]/[path/]file[?param=value or /value of param]`

##### 3) Các HTTP header:

- **Host**: chỉ định tên máy chủ cùng với số port của máy chủ mà request đang gửi đến.
- **Location**: được sử dụng trong các response chuyển hướng (những response có status code là `3xx` (redirection) hoặc `201` (created)) để xác định URL mà page muốn chuyển hướng đến.
- **Cookie**: chứa các HTTP cookie liên quan đến server (có thể được gửi tới client từ trước bởi server với header là **Set-Cookie** hoặc được tạo bằng Javascript thông qua lệnh `Document.cookie`).
- **Referer**:  chứa địa chỉ tuyệt đối hoặc một phần của trang đã tạo ra request. Khi nhấp vào một liên kết, đây sẽ là địa chỉ của trang chứa liên kết. Khi thực hiện các yêu cầu tài nguyên đến một miền khác, đây sẽ là địa chỉ của trang sử dụng tài nguyên. 
- **Content-Length**: chỉ định độ dài của nội dung message, tính bằng byte (ngoại trừ trường hợp responses đối với HEAD requests, khi nó chỉ ra độ dài của nội dung trong responses đối với GET requests tương ứng).
- **Cache-Control**: chứa các directives (chỉ thị) quy định cách thức, địa chỉ để ghi vào bộ đệm đối với requests và response.
- **Connection**: cho đầu kia của phiên giao tiếp (transaction) biết liệu nó có nên đóng kết nối TCP sau khi quá trình truyền message hoàn tất hay giữ nó mở cho các message tiếp theo. Nếu header này có giá trị là `keep-alive`, kết nối vẫn được tiếp tục.
- **Range**: chỉ định phạm vi của documnet mà server cần phải gửi đến. Nếu server trả về với đúng phạm vi trong request, reponse sẽ trả về status code là 206 (Partial Content). Nếu giá trị của **Range** là không hợp lệ, reponse sẽ trả về status code là 416 (Range Not Satisfiable). Nếu server bỏ qua **Range** header và trả về toàn bộ nội dung của document thì reponse sẽ trả về status code 200.
- **Strict-Transport-Security**: là một reponse header cho phép website yêu cầu rằng liệu trình duyệt có cần phải truy cập nó thông qua HTTPS thay vì HTTP hay không.
- **Access-Control-Allow-***: cho biết liệu tài nguyên có thể được truy xuất thông qua các cross-domain Ajax requests hay không.

##### 4) CSP (Content Security Policy):

CSP là một lớp bảo mật bổ sung giúp phát hiện và giảm thiểu một số loại tấn công nhất định, bao gồm Cross Site Scripting (XSS) và các cuộc tấn công chèn dữ liệu. Các cuộc tấn công này được sử dụng cho mục đích từ đánh cắp dữ liệu đến phá hoại trang web hay phát tán phần mềm độc hại. Một ví dụ về CSP yếu: 

https://github.com/antoinenguyen-09/All_CTF_write-ups/blob/master/diceCTF_2_2021/Web%20Exploitation/Babier%20CSP.md

##### 5)  SOP (Same Origin Policy):

SOP là một cơ chế bảo mật quan trọng nhằm hạn chế việc một tài liệu hoặc tập lệnh được tải từ một nguồn có thể tương tác với tài nguyên từ một nguồn khác. Nó giúp cô lập các tài liệu độc hại tiềm ẩn, giảm các nguy cơ tấn công có thể xảy ra.

##### 6) HTTP Only:

HttpOnly là một flag được bổ sung trong Set-Cookie HTTP response header. Việc sử dụng flag HttpOnly khi tạo cookie giúp giảm thiểu rủi ro client side script truy cập vào cookie đang được bảo vệ.

##### 7) Các flag của một cookie:

* **expire**: đặt một thời điểm cho đến khi cookie hết hạn. Điều này khiến trình duyệt lưu cookie vào bộ nhớ liên tục và nó được sử dụng lại trong các phiên trình duyệt tiếp theo cho đến khi đạt đến thời điểm hết hạn. Nếu flag này không được đặt, cookie chỉ được sử dụng trong phiên trình duyệt hiện tại.
* **domain**: chỉ định domain mà cookie được coi là hợp lệ. Tên miền này phải giống nhau hoặc cùng tên miền mà từ đó cookie được nhận.
* **path**: chỉ định đường dẫn URL mà cookie được coi là hợp lệ.
* **secure**: nếu flag này được đặt, cookie sẽ chỉ được gửi trong các HTTPS requests.
* **HttpOnly** đã được đề cập ở trên.

##### 8) Các mã trả về của HTTP Response:

<p>Mỗi thông báo HTTP repsonse phải chứa mã trả về trong dòng đầu tiên của nó, cho biết kết quả của các requests. Các mã trả về (status code) được chia thành 5 nhóm, theo chữ số đầu tiên của các mã:</p>

- 1xx - Thông tin
- 2xx - Request thành công
- 3xx - Máy client được chuyển hướng đến một tài nguyên khác
- 4xx - Request gặp lỗi
- 5xx - Máy chủ gặp lỗi khi thực hiện request.

<p>Có rất nhiều mã trả về cụ thể, nhiều mã chỉ được sử dụng trong các trường hợp đặc biệt. Dưới đây là các mã trả về có khả năng gặp nhất khi tấn công một ứng dụng web:</p>

* `100 Continue`: được gửi trong một số trường hợp khi client gửi yêu cầu có chứa nội dung. Respone chỉ ra rằng các request header đã được nhận và client sẽ tiếp tục gửi nội dung. Máy chủ trả về response thứ hai khi request đã được hoàn thành.
* `200 OK`: cho biết rằng request đã thành công và response sẽ chứa kết quả của request.
* `201 Created`: được trả về để phản hồi một yêu cầu PUT để cho biết rằng request đã thành công.
* `301 Moved Permanently`: chuyển hướng trình duyệt vĩnh viễn đến một URL khác, được chỉ định trong `Location` header. Client nên sử dụng URL mới trong tương lai thay vì URL ban đầu.
* `302 Found`: chuyển hướng trình duyệt tạm thời đến một URL khác, được chỉ định trong `Location` header. Client sẽ trở về URL ban đầu trong các request tiếp theo.
* `304 Not Modified`: hướng dẫn trình duyệt sử dụng bản sao được lưu trong bộ nhớ cache của tài nguyên được yêu cầu. Máy chủ sử dụng request header `If-Modified-Since` và `If-None-Match` để xác định xem client có phiên bản mới nhất của tài nguyên hay không.
* `400 Bad Request`: cho biết rằng client đã gửi một HTTP request không hợp lệ. Client có thể sẽ gặp phải điều này khi họ đã sử đổi một request theo những cách không hợp lệ chẳng hạn như bằng cách đặt một ký tự không hợp lý vào URL.
* `401 Unauthorized`: chỉ ra rằng máy chủ yêu cầu xác thực HTTP trước khi request được thực hiện. Header `WWW-Authenticate` chứa thông tin chi tiết về các loại xác thực được hỗ trợ.
* `403 Forbidden`: chỉ ra rằng không ai được phép truy cập tài nguyên được yêu cầu, kể cả đã được xác thực.
* `404 Not Found`: chỉ ra rằng tài nguyên được yêu cầu không tồn tại.
* `405 Method Not Allowed`: cho biết rằng method được sử dụng trong request không được hỗ trợ cho URL được chỉ định.
* `413 Request Entity Too Large`: nếu hacker đang tìm kiếm lỗ hổng buffer overflow trong mã nguồn và khi đó gửi một chuỗi dữ liệu dài, mã trả về này cho biết phần nội dung của request quá lớn để máy chủ có thể xử lý.
* `414 Request URI Too Long`: tương tự như mã 413. Nó chỉ ra rằng URL được sử dụng trong request quá lớn để máy chỉ có thể xử lý.
* `500 Internal Server Error`: cho biết rằng máy chủ đã gặp lỗi khi thực hiện yêu cầu. Điều này thường xảy ra khi người dùng gửi thông tin đầu vào không như mong muốn và gây ra lỗi chưa được khắc phục ở đâu đó trong quá trình xử lý ứng dụng. Người dùng nên xem xét kỹ toàn bộ nội dung response của máy chủ để biết chi tiết nào chỉ ra tình trạng của lỗi.
* `503 Service Unavailable`: thường chỉ ra rằng, mặc dù bản thân máy chủ web đang hoạt động và có thể phản hồi các request nhưng ứng dụng được truy cập qua máy chủ lại không phải hồi. Người dùng nên xem lại xem đây có phải là kết quả của bất kỳ hành động nào họ đã thực hiện hay không.

### II. Thực hành:

##### 1) HTTP Client **GET**:

- Source of client_get.py: https://github.com/antoinenguyen-09/Socket-Programming/edit/main/client.py
- Output:

![image](https://user-images.githubusercontent.com/61876488/118679305-fb0b7700-b827-11eb-836c-93fb5b77174f.png)

##### 2) HTTP Client POST:

- Source of client_post.py: https://github.com/antoinenguyen-09/Socket-Programming/blob/main/client_post.py

##### 3) HTTP Client upload:

- Source of upload.py: https://github.com/antoinenguyen-09/Socket-Programming/blob/main/upload.py
- Output:

![image](https://user-images.githubusercontent.com/61876488/118694812-ae7b6800-b836-11eb-9fc9-eeb5af7380d3.png)

##### 4) HTTP Client download:

- Source of download.py:  https://github.com/antoinenguyen-09/Socket-Programming/blob/main/download.py
- Output:

![image](https://user-images.githubusercontent.com/61876488/118696329-61989100-b838-11eb-9224-2fa0ab80f8a3.png)





