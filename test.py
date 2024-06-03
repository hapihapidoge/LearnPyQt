import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox

class MortgageCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # 创建标签和输入框
        self.loan_amount_label = QLabel('贷款金额 (元):', self)
        self.loan_amount_input = QLineEdit(self)
        
        self.annual_rate_label = QLabel('年利率 (%):', self)
        self.annual_rate_input = QLineEdit(self)
        
        self.loan_term_label = QLabel('贷款期限 (年):', self)
        self.loan_term_input = QLineEdit(self)
        
        self.calculate_button = QPushButton('计算月供', self)
        self.calculate_button.clicked.connect(self.calculate_mortgage)
        
        self.result_label = QLabel('', self)
        
        # 布局
        vbox = QVBoxLayout()
        vbox.addWidget(self.loan_amount_label)
        vbox.addWidget(self.loan_amount_input)
        
        vbox.addWidget(self.annual_rate_label)
        vbox.addWidget(self.annual_rate_input)
        
        vbox.addWidget(self.loan_term_label)
        vbox.addWidget(self.loan_term_input)
        
        vbox.addWidget(self.calculate_button)
        vbox.addWidget(self.result_label)
        
        self.setLayout(vbox)
        
        # 窗口属性
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('房贷计算器')
        self.show()
        
    def calculate_mortgage(self):
        try:
            loan_amount = float(self.loan_amount_input.text())
            annual_rate = float(self.annual_rate_input.text())
            loan_term = int(self.loan_term_input.text())
            
            monthly_rate = annual_rate / 12 / 100
            number_of_payments = loan_term * 12
            
            if monthly_rate == 0:
                monthly_payment = loan_amount / number_of_payments
            else:
                monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** number_of_payments) / ((1 + monthly_rate) ** number_of_payments - 1)
            
            self.result_label.setText(f'每月支付金额: {monthly_payment:.2f} 元')
        except ValueError:
            QMessageBox.warning(self, '输入错误', '请输入有效的数字')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MortgageCalculator()
    sys.exit(app.exec_())
