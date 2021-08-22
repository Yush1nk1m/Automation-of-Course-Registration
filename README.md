# Automation-of-Course-Registration
https://www.python.org/
프로그램 사용 전 python 최신 버전을 반드시 다운로드 하세요.
권장 설정으로 다운로드 하시면 됩니다.

이 프로그램들은 python 언어 기반으로 만든 자동 클릭 프로그램으로,
사용자가 매분 몇 초에 버튼을 클릭할지 설정하면 그 시간에 맞추어 "로그인(Log-in)" 버튼
또는 "다시 로그인하기(Re-Login)" 버튼을 클릭합니다.

사용자가 직접 컴퓨터의 "시스템 시간"과 서강대학교 수강신청 페이지 "서버 시간" 간의 시차를 찾아내야 하므로
적어도 수강신청 20분 전부터는 매분 측정해 보시기 바랍니다.

파일마다 역할이 다르므로 설명서를 잘 읽어주십시오.

@@ 원리
우리는 평소에 수강신청을 할 때 네이비즘 시계를 밀리초 단위로 켜놓고 로그인 버튼을 눌러보면서 타이밍을 맞춰보곤 합니다.
그런데 이 방식은 변수가 너무 많습니다. 대표적으로 떠올릴 수 있는 변수만 해도
1. 사람의 반응 속도가 일정하지 않다. ( ex : 59.7초 때 클릭하려고 했는데 59.5초에 예측 클릭해서 튕기는 상황)
2. 네이비즘 시계를 밀리초 단위로 켜두면 서버 시간과 맞지 않게 점점 느려질 때가 있다.
등이 있습니다.

그래서 컴퓨터가 사용하고 있는 "시스템 시간"을 기준으로 "서버 시간"과의 시차를 발견해
돌아오는 1분 뒤 설정한 초에 로그인 버튼을 클릭하는 프로그램을 만들었습니다.
예를 들어, 9시 58분 13초에 실행하여 1.2초로 설정 시 돌아오는 9시 59분 1초 20쯤에 컴퓨터가 로그인 버튼을 클릭하게 됩니다.

딱 한 번 클릭하고 꺼지는 프로그램으로, 여러 번 실행해보며 시차를 맞추어 보면 됩니다.

수강신청 당일에는 로그인 시도가 증가함에 따라 우리가 로그인을 클릭했을 때 이 신호가 서버로 전달되는 속도가 점점 느려집니다.
예를 들어 평소에는 59초 90에 클릭했을 때 정각에 들어갔는데, 수강신청 당시에는 0.1~2초 정도 밀려 59초 70에 클릭한 사람이 정각에
들어가게 되는 일도 생기는 것입니다.

그렇기에 이 프로그램이 "안전빵"을 보장한다고 할 수 있습니다.
수강신청 20분 전쯤 우리가 시차를 0.2초로 맞추었다고 합시다. 매분 0초 20에 클릭하는 것입니다.
그러면 수강신청 때 이 시차가 0.1초에서 0.2초 정도 느려지면 느려지지 더 빨라지진 않기 때문에
59초에 클릭해서 튕기고 시간표가 망하는 경험을 하지 않아도 됩니다.

야수의 심장을 갖고 있다면 이렇게 수강신청 당시 0.1~2초 정도 느려지는 것을 생각해
기존에 맞춰두었던 시차보다 0.1초 정도 일찍 들어갈 수도 있습니다.

어떻게 사용하는지는 사용자에게 달려있습니다.

@@ 주의사항
시간은 무조건 X.X초, 소수점 한 자리수까지만 입력해야 합니다. 아니면 오류가 발생할 수 있습니다.
그리고 0.0초보다 0.1초 빠르게 하려면 -0.1이 아니라 59.9를 입력해야 합니다.
왜냐하면 10시 00분 "00초 00"의 0.1초 전은 10시 00분 00초 -10이 아니라 9시 59분 "59초 90"이기 때문입니다.

@@ TIP
처음에 0.0초를 입력해 실행합니다. 
서버 시간이 59초로 나온다면 0.1초씩 늘리고, 00초로 나온다면 0.1초씩 줄이면서 최적의 시차를 발견하면 됩니다.
예를 들어 0.0초를 입력해서 59초가 나왔고, 0.1초씩 늘리다가 0.3초에서 처음으로 00초가 나왔다고 합시다.
그러면 시스템 시간과 서버 시간의 시차는 0.3초 정도(정확히 0.3초는 아닐 것입니다.)라고 할 수 있고,
이것이 최적의 설정값이 되는 것입니다.


@ mouse_crd
마우스 좌표를 잡아주는 프로그램입니다.
크롬을 전체 화면으로 켜두지 않았더라도 로그인 버튼을 좌표에 맞추어 위치시키면 잘 클릭합니다.

@ pip_install
프로그램 안의 코드가 실행될 수 있도록, 그 기반이 되는 도구를 설치하는 프로그램입니다.
python이 컴퓨터에 설치된 후 한 번은 무조건 실행해줘야 합니다.
"관리자 권한으로 실행"해 주시기 바랍니다.

@ re-login_click
수강신청 당일이 아닌 경우, 로그인 버튼을 눌렀을 때 나오는 수강신청 접속 제한 안내 페이지에서
서버 시간을 알려주지 않습니다. 대신 이때 "다시 로그인하기(Re-Login)" 버튼을 눌러서 수강신청 홈페이지로
복귀하면 서버 시간을 알려주게 되는데, 이렇게 서버 시간과 시스템 시간의 차이를 확인하기 위한 프로그램입니다.

해상도 1920 * 1080, 크롬 브라우저 전체 화면 기준으로 마우스 좌표를 잡았기 때문에 동일한 환경에서의 실행을 권장합니다.
또는 "다시 로그인하기(Re-Login)" 버튼을 (x, y) = (726, 467) 좌표에 위치시켜 주십시오.

수강신청 당일에는 이 프로그램이 아닌 login_click 프로그램으로 연습할 것을 권장합니다.

@ login_click
수강신청 당일에는 로그인 버튼을 눌렀을 때 나오는 수강신청 접속 제한 안내 페이지에서 서버 시간을 알려줍니다.
그러므로 이 프로그램만으로 시스템 시간과 서버 시간 간의 차이를 측정할 수 있고, 당연하게도 수강신청 때는
이 프로그램을 사용하게 됩니다.

해상도 1920 * 1080, 크롬 브라우저 전체 화면 기준으로 마우스 좌표를 잡았기 때문에 동일한 환경에서의 실행을 권장합니다.
또는 "로그인(Log-in)" 버튼을 (x, y) = (1200, 330) 좌표에 위치시켜 주십시오.

