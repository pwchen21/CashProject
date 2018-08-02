"""
Version:0.0.01
Histroy: 
2018/8/1 - Initial Version

Waiting Imporve / Fix:
F001- Shows select record when using Tab to change column 

Modify Date: 2018/8/1
"""

import pickle
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class InitCredit:

	def __init__(self):
		# Create InitCredit
		self.IC=tk.Tk()
		self.IC.title("Init/Edit Credit")
		self.IC.geometry('310x260')
		
		# Create Credit Card List
		self.cdstr=tk.StringVar()
		self.getcd='select BANK,TYPE from INIT_CREDIT'
		self.cdstr.set(self.conn_db(self.getcd))
		tk.Label(self.IC, text="信用卡列表：").place(x=33, y=10)
		self.cdlb=tk.Listbox(self.IC, listvariable=self.cdstr, width=15, height=12)
		self.cdlb.place(x=10, y=30)
		#self.cdlb.bind('<<ListboxSelect>>', self.selected)
			
		# Create Bank Name
		self.CBS=tk.StringVar()
		tk.Label(self.IC, text="銀行名稱：").place(x=130, y=10)
		self.CB=tk.Entry(self.IC, width=13, textvariable=self.CBS)
		self.CB.place(x=200, y=10)
			
		# Create credit card name
		self.CDNS=tk.StringVar()
		tk.Label(self.IC, text="卡種：").place(x=130, y=40)
		self.CDNE=tk.Entry(self.IC, width=8, textvariable=self.CDNS)
		self.CDNE.place(x=200, y=40)
			
		# Create Credit card type	
		self.CDTS=tk.StringVar()
		option=['Master', 'Visa', 'JCB']
		tk.Label(self.IC, text="卡別：").place(x=130, y=70)
		self.CDTOM=ttk.OptionMenu(self.IC, self.CDTS, option[0], *option)
		self.CDTOM.place(x=200, y=70)

		"""
		# Create CURRENT Deposit
		self.CCDS=tk.StringVar()
		tk.Label(self.IC, text="活期存款：").place(x=130, y=140)
		self.CCD=tk.Entry(self.IC, width=13, textvariable=self.CCDS)
		self.CCD.place(x=200, y=140)
				
		# Create FIX Deposit
		self.CFDS=tk.StringVar()
		tk.Label(self.IC, text="定期存款：").place(x=130, y=170)
		self.CFD=tk.Entry(self.IC, width=13, textvariable=self.CFDS)
		self.CFD.place(x=200, y=170)

		# Create Button for New / Save / Cancel
		NBBT=tk.Button(self.IC, text="Add", bg='gray94', bd=2, command=self.new_bank)
		NBBT.place(x=130, y=210)
		SBBT=tk.Button(self.IC, text="Save", bg='gray94', bd=2, command=self.save_bank)
		SBBT.place(x=180, y=210)
		CBBT=tk.Button(self.IC, text="Del", bg='gray94', bd=2, command=self.del_bank)
		CBBT.place(x=230, y=210)		
		
		"""	
		self.IC.mainloop()
	
	def conn_db(self, sqlc, *v):		
			conn=sqlite3.connect(r'db/test.db')
			c=conn.cursor()
			r=c.execute(sqlc, *v)
			data=r.fetchall()
			conn.commit()
			conn.close()
			return data
	
	"""
	# Clear all entry
	def clear_all(self):
		self.CB.delete(0, 'end')
		self.CBB.delete(0, 'end')
		self.CBA.delete(0, 'end')
		self.CCD.delete(0, 'end')
		self.CFD.delete(0, 'end')	
	
	def selected(self, *w):
		try:
			value=self.bklb.get(self.bklb.curselection())[0]
			sql="SELECT * FROM INIT_BANK WHERE TITLE=?"
			get_record=self.conn_db(sql, (value,))
			self.CBS.set(get_record[0][1])
			self.CBBS.set(get_record[0][2])
			self.CBAS.set(get_record[0][3])
			self.CCDS.set(get_record[0][4])
			self.CFDS.set(get_record[0][5])
		except:
			tk.messagebox.showerror(title='Error', message='Please select record!!')

		
	def new_bank(self):	
		sql='INSERT INTO INIT_BANK (TITLE, CODE, ACCOUNT, CUR_DEP, FIX_DEP) VALUES (?,?,?,?,?)'
		self.conn_db(sql, (self.CB.get(), self.CBB.get(), self.CBA.get(), self.CCD.get(), self.CFD.get()))
		#Rebuild list
		self.bankstr.set(self.conn_db(self.getbank))
		
		self.clear_all()
		
	def save_bank(self):
		value=self.bklb.get(self.bklb.curselection())[0]
		sql='UPDATE INIT_BANK SET TITLE=?, CODE=?, ACCOUNT=?, CUR_DEP=?, FIX_DEP=? WHERE TITLE=?'
		self.conn_db(sql, (self.CBS.get(), self.CBBS.get(), self.CBAS.get(), self.CCDS.get(), self.CFDS.get(), value,))
		#Rebuild list
		self.bankstr.set(self.conn_db(self.getbank))

		
	def del_bank(self):
		value=self.bklb.get(self.bklb.curselection())[0]
		sql='DELETE FROM INIT_BANK WHERE TITLE=?'
		self.conn_db(sql, (value,))
		#Rebuild list
		self.bankstr.set(self.conn_db(self.getbank))
		
		self.clear_all()
	"""
	
InitCredit()
