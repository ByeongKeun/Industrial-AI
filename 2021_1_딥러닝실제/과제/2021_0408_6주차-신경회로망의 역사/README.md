# 6주차 과제
 - 신경회로망의 역사조사 - 최소 3page
 - 2021.04.12(월) 제출
 - 산출물: 조사 자료

<p> <img src="https://github.com/ByeongKeun/Industrial-AI/blob/master/images/dnn_history1.png" border="0" width="100" height="150"> </p>

**한글: 인공신경망**

**한문: 人工神經網,** 

**영어: artificial neural network, ANN)**


**1. 정의**

사람 또는 동물 두뇌의 신경망에 착안하여 구현된 컴퓨팅 시스템의 총칭.

기계 학습(machine learning)의 세부 방법론 중 하나로, 신경 세포인 뉴런(neuron)이 여러 개 연결된 망의 형태이다. 

구조 및 기능에 따라 여러 종류로 구분되며, 가장 일반적인 인공 신경망은 한 개의 입력층과 출력층 사이에 다수의 은닉층(hidden layer)이 있는 다층 퍼셉트론(multilayer perceptron)이다.

인공 신경망은 하드웨어로 구현될 수도 있으나, 주로 컴퓨터 소프트웨어로 구현된다. 인공 신경망은 기초 컴퓨팅 단위인 뉴런 여러 개가 가중된 링크(weighted link)로 연결된 형태이다. 

가중된 링크(weighted link)는 주어진 환경에 적응할 수 있도록 가중치를 조정할 수 있다.

인공 신경망은 자기 조직화 지도(SOM: Self-Organizing Map), 순환 신경망(RNN: Recurrent Neural Network), 콘볼루션 신경망(CNN: Convolutional Neural Network)과 같은 다양한 모델에 대한 총칭으로, 그 종류는 수십 가지에 이른다.

오늘날 신경망은 판독기, 일기 예보, 폭탄 탐지기, 심지어 금융시장 예측에서 이용되는 광학식 문자판독 기반 기술로 사용되고 있다.



**2. 역사**

**1943 “인공신경망의 기원”**

워런 맥컬록(Warren McCulloch)와 월터 피츠(Walter Pitts)의 뉴런의 2진법 논리모델화

논문 발표“A logical calculus of the ideas immanent in nervous activity”
<p> <img src="https://github.com/ByeongKeun/Industrial-AI/blob/master/images/dnn_history2.png" border="0" width="500" height="300"> </p>

단위 뉴런의 동작은 단순하나 이러한 뉴런들이 연결되어 하나의 뇌와 같은 네트워크를 이루고 이 네트워크는 보다 복잡한 문제도 해결할 수 있다는 것을 설명하고 있으며, 이 논문이 인공 신경망의 기원이라는 의의를 갖는 것은 생물학적 뉴런의 네트워크를 기계적으로 모델링한 것에 있습니다

**1949 “Hebb의 법칙”**

심리학자 도널드 헤비안(Donald Hebb)는 헤비안 학습(Hebbian learning)이라 불리는 신경가소성의 원리에 근거한 학습의 기본 가정을 만들었습니다. 헤비안 학습은 전형적인 자율학습으로 이것의 변형들은 장기강화(long term potentiation)의 초기 모델이 되었습니다

실제 뇌과학적인 원리를 통한, 인공신경망의 학습규칙으로서, 모든 생물이 그러하듯 스스로 학습하고 변화하는 알고리즘을 인공신경망이 어떤 식으로 내포하는지에 대한 학습규칙을 정의

**1954 “계산기”**

팔리(Farley)와 웨슬리 클라크(Wesley A. Clark)는 MIT에서 헤비안 네트워크를 모의 실험하기 위해 처음으로 계산학 모델(후에 계산기라 불리는)을 사용하였습니다

※(1956)다른 신경망 계산학 기계들은 로체스터(Rochester), 홀랜드(Holland), 하빗(Habit), 두다(Duda)에 의해 만들어졌다.

**1958 “퍼셉트론”**

프랑크 로젠블라트(Frank Rosenblatt)는 퍼셉트론 즉, 간단한 덧셈과 뺄셈을 하는 이층구조의 학습 컴퓨터 망에 근거한 패턴 인식을 위한 알고리즘을 만들었습니다. 

계산학 표기법과 함께 로벤블라트는 또한 기본적인 퍼셉트론에 대한 회로가 아닌, 예를 들면 배타적 논리합 회로(exclusive-or circuit)와 같은 회로를 표기하였습니다. ※(1975) 해당 회로의 수학 계산은 폴 웨어보스(Paul Werbos)에 의해 오차역전파법이 만들어진 후에 가능하게 되었습니다

로젠블라트 모형은, 아직까지도 기본적인 인공신경망 모델로써 참고가 됩니다.

**1969 “1차 암흑기”**

마빈 민스키(Marvin Minsky)와 시모어 페퍼트(Seymour Papert)에 의해 기계학습 논문이 발표된 후에 신경망 연구는 침체되었습니다. 그들은 인공신경망에서 두 가지 문제점을 찾아내었습니다. 

첫 번째로는 단층 신경망은 배타적 논리합 회로를 처리하지 못한다는 것이다. 

두 번째 중요한 문제는 거대한 신경망에 의해 처리되는 긴 시간을 컴퓨터가 충분히 효과적으로 처리할 만큼 정교하지 않다는 것이다. 

즉, 기존 로젠블라트와 그를 기반으로 개선된 아달린 모델을 수학적으로 분석하며, 그 한계를 지적하고 가장 긱본적인 XOR분류조차 해당모델로 수행하지 못함을 밝혀냈습니다

이로 인해 신경망 연구는 컴퓨터가 충분히 빨라지고, 배타적 논리합 문제를 효율적으로 처리하는 오차역전파법이 만들어지기까지 더디게 진행되었습니다.

**1982 “Perceptron 문제 해결”**

Hopefield에 의한 Perceptron에서의 문제점 해결, 해답은 다층 신경망(MLP : Multi-Layer Perceptron)에 있었습니다. 

실제 XOR 게이트도 다른 기본 게이트를 결합하여 만들 듯, 

인공신경망 역시, 기존의 단층이 아닌 다층으로 쌓아서 만드는 것으로, 선형 분류에서 벗어나, 현실적인 모든 문제를 분류할 수 있게 되었습니다.(이로써 인공신경망 연구에 다시 불이 붙습니다.)

<p> <img src="https://github.com/ByeongKeun/Industrial-AI/blob/master/images/dnn_history3.png" border="0" width="372" height="245"> </p>
※MLP 구조: <입력층> - <히든레이어 : 다층 신경망> - <출력층>

**1986** 

데이비드 럼멜하트(David E. Rumelhart)와 제임스 맥클레랜드(James McClelland)가 쓴 교과서는 연결주의를 이용해 신경 처리를 컴퓨터에서 모의 실험하기 위한 모든 것을 설명하였습니다

인공신경망이 어느정도 뇌의 기능을 반영하는지 불분명하기 때문에 뇌 신경 처리의 간단한 모델과 뇌 생물학적 구조간의 상관관계에 대해 논란 중에 있으나 인공지능에서 사용되는 신경망은 전통적으로 뇌 신경 처리의 간단한 모델로 간주되고 있습니다

**1989 “2차 침체기”**

얀 르쿤(Yann Lecun)의 “Handwritten digit recognition with a back-propagation network” 필기숫자 인식(MNIST)문제에 적용하는 실용적인 논문을 발표

오류역전파 알고리즘(Backpropagation Algorithm)에 기반하여 우편물에 쓰여진 우편번호를 인식하는 알고리즘을 소개했다. 다만 신경망 학습에 소요되는 시간이 (10개 숫자) 3일이 걸렸고, 이것은 다른분야에 일반적으로 적용되기에는 비현실적인 것으로 여겨졌다

**2006 “Deep Network, Deep Learning의 용어출현”**

제프리 힌턴(Geoffery Hinton)의 논문 "A fast learning algorithm for deep belief nets" 심층 신뢰망(DBN, Deep-Belief Network)의 등장

RBM(Restricted Boltzman Machine, 적층제약 볼츠먼 머신), 모든 노드는 자신을 제외한 다른 노드들과 연결되어 있으며 이러한 속성으로 인해 순환적인 모델을 만들 수 있습니다.

심층 신뢰망(DBN)은 RBM을 여러 개의 층으로 구성된 신경망으로써, 탐욕적인 층별 사전훈련(Greedy layer-wise pretraining)알고리즘을 적용하여, 역전파시에 가중치가 0에 가까워지는 문제를 해결 하였습니다

<p> <img src="https://github.com/ByeongKeun/Industrial-AI/blob/master/images/dnn_history4.png" border="0" width="686" height="306"> </p>

**※ 당시 논문들은 Neural network라는 단어가 들어가면 논문에 거절당하는 말이 있을 정도로 신경망이 외면 받던 시기 였습니다**

**2012 “딥러닝의 저력”**

IMAGENET이라는 이미지 분류 대회에서 알렉스(제프리 힌튼 교수의 제자)가 알렉스넷(AlexNet)이라는 딥러닝 기반 알고리즘으로 84.7%의 정확도로 분류 하였습니다.

80%이상의 인식률은 거의 불가능이라는 인식이 있을 당시였기에 충격적인 사건이었고, 이후 대부분의 참가팀들이 알고리즘을 딥러닝으로 방향을 돌리는 계기가 되었습니다

<p> <img src="https://github.com/ByeongKeun/Industrial-AI/blob/master/images/dnn_history5.png" border="0" width="296" height="369"> </p>


**2016 “AlphaGo”**

구글 딥마인드의 알파고와 이세돌 9단의 대국에서, 4:1로 승리하였습니다
<p> <img src="https://github.com/ByeongKeun/Industrial-AI/blob/master/images/dnn_history6.png" border="0" width="313" height="369"> </p>
