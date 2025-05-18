menu = True
while menu:
	message = """
	--Hello user--
	Welcome to your phone Menu
	press any of the following to start:

	1: Phone book
	2: Message
	3: Chat
	4: Call register
	5: Tone
	6: Settings
	7: Call divert
	8: Games
	9: Calculator
	10: Remainders
	11: Clock
	12: Profiles
	13: SIM service
	0: Exit

	"""
	print(message)

	select = int(input())

	match select:
		case 1:
			phonebookMenu = True
			while phonebookMenu:
				print("Welcome to Phone book")
		
				message = """
				press a number:

				1: Search
				2: Service Nos
				3: Add name
				4: Erase
				5: Edit  
				6: Assign tone
				7: Send b'card
				8: Options
				9: Speed dials
				10: Voice tags
				0: Exit
				"""
				print(message)
		

				select = int(input())
				match select:
					case 1:
						search = True
						while search:
							print("Welcome to Search")
							message = """
							press a number:
	
							0: Return to phonebook
	
							"""
							print(message)
							selectPhonebook = int(input())
	
							match(selectPhonebook):
								case 0: search = False

								case _ : print("Invalid - Try again")


					case 2:
						serviceNos = True
						while(serviceNos):
							print("Welcome to serviceNos")
							message = """
							press a number:
	
							0: Return to phonebook

							"""
							print(message)
							selectPhonebook = int(input())
	
							match(selectPhonebook):
								case 0: serviceNos = False
	
								case _: print("Invalid - Try again")


					case 3:
						Addname = True
						while(Addname):
							print("Welcome to Add name");
							message = """
							press a number:
	
							0: Return to phonebook
	
							"""
							print(message);
							selectPhonebook = int(input())
							match(selectPhonebook):
								case 0: Addname = false
		
								case _: print("Invalid - Try again")

					case 4:
						Erase = true
						while(Erase):
							print("Welcome to Erase");
							message = """
							press a number:
	
							0: Return to phonebook
				
							"""
							print(message)
							selectPhonebook = int(input())
							match(selectPhonebook):
								case 0: Erase = False
								case _: print("Invalid - Try again")


					case 5:
						Edit = True
						while(Edit):
							print("Welcome to Edit")
							message = """
							press a number:

							0: Return to phonebook

							"""
							print(message)
							selectPhonebook = int(input())
	
							match(selectPhonebook):
								case 0: Edit = False
								case _: print("Invalid - Try again")

					case 6:
						AssignTone = True
						while(AssignTone):
							print("Welcome to Assign Tone")
							message = """
							press a number:
							0: Return to phonebook
							"""
							print(message)
							selectPhonebook = int(input())
							match(selectPhonebook):
								case 0: AssignTone = False
								case _: print("Invalid - Try again")


					case 7:
						Sendbcard = True
						while(Sendbcard): 
							print("Welcome to Send b' card")
							message = """
							press a number:
							0: Return to phonebook
							"""
							print(message)
							selectPhonebook = int(input())
							match(selectPhonebook):
								case 0: Sendbcard = False
								case _: print("Invalid - Try again")


					case 8:
						Options = True
						while(Options): 
							print("Welcome to Options")
							message = """
							press a number:
							1: Type of view
							2: Memory status
							0: go back to options
							"""
							print(message);
							select = int(input())
							match(select):
								case 1:
									Typeofview = True
									while(Typeofview): 
										print("Welcome to Types of view")
										message = """
										press a number:
										0: Return to phonebook
										"""
										print(message)
										selectPhonebook = int(input())
										match(selectPhonebook):
											case 0: Typeofview = False
											case _: System.out.println("Invalid - Try again");


								case 2:
									MemoryStatus = True
									while(MemoryStatus): 
										print("Welcome to Memory Status")
										message = """
										press a number:
										0: Return to phonebook
										"""
										print(message)
										selectPhonebook = int(input())           
										match(selectPhonebook):
											case 0: MemoryStatus = False
											case _: print("Invalid - Try again")


								case 0: Options = False
								case _: print("Invalid - Try again")



					case 9:
						Speeddials = True
						while(Speeddials): 
							print("Welcome to Speed dials")
							message = """
							press a number:
							0: Return to phonebook
							"""
							print(message)
							selectPhonebook = int(input())
							match(selectPhonebook):
								case 0: Speeddials = False
								case _: print("Invalid - Try again");


					case 10:
						VoiceTags = True
						while(VoiceTags): 
							print("Welcome to Voice Tags")
							message = """
							press a number:
							0: Return to phonebook
							"""
							print(message)
							selectPhonebook = int(input())
							match(selectPhonebook):
								case 0: VoiceTags = False
								case _: print("Invalid - Try again")


					case 0:
						phonebookMenu = False
					case _: print("Who you be???... Do am again");





		case 2:
			Messages = True
			while(Messages): 
				print("Welcome to Messages")
	
	
				message = """
				press a number:
	
				1: Write message
				2: Inbox
				3: Outbox
				4: Picture message
				5: Templates
				6: Smileys
				7: Message settings
				8: Info service
				9: Voice mailbox number
				10: Service command editor
				0: Return to menu
	
				"""
				print(message)
				select = int(input())
				match(select):
	
					case 1:
						Writemessage = True
						while(Writemessage): 
							print("Welcome to Writemessage")
							message = """
							press a number:
	
							0: Return to Messages
	
							"""
							print(message)
							selectPhonebook = int(input())
	
							match(selectPhonebook):
								case 0: Writemessage = False
	
								case _: print("Invalid - Try again")
	
	
	
					case 2:
						Inbox = True
						while(Inbox): 
							print("Welcome to Inbox")
							message = """
							press a number:
	
							0: Return to Messages
	
							""";
							print(message);
							selectPhonebook = int(input())
	
							match(selectPhonebook):
								case 0: Inbox = False
	
								case _: print("Invalid - Try again")
	
	
	
					case 3:
						Outbox = True
						while(Outbox): 
							print("Welcome to Outbox")
							message = """
							press a number:
	
							0: Return to Messages
	
							"""
							print(message)
							selectPhonebook = int(input())
	
							match(selectPhonebook):
								case 0: Outbox = False
	
	
								case _: print("Invalid - Try again")
	
	
	
					case 4:
						PictureMessage = True
						while(PictureMessage): 
							print("Welcome to PictureMessage")
							message = """
							press a number:
	
							0: Return to Messages
	
							"""
							print(message);
							selectPhonebook = int(input())
	
							match(selectPhonebook):
								case 0: PictureMessage = False
	
	
								case _: print("Invalid - Try again")
	
	
	
					case 5:
						Templates = true;
						while(Templates): 
							print("Welcome to Templates")
							message = """
							press a number:
	
							0: Return to Messages
	
							"""
							print(message)
							selectPhonebook = int(input())
	
							match(selectPhonebook):
								case 0: Templates = False
	
	
								case _: print("Invalid - Try again")
	
	
	
					case 6:
						Smileys = true;
						while(Smileys): 
							print("Welcome to Smileys")
							message = """
							press a number:
	
							0: Return to Messages
	
							"""
							print(message);
							selectPhonebook = int(input())
	
							match(selectPhonebook):
								case 0: Smileys = False
	
	
								case _: print("Invalid - Try again")
	
	
	
					case 7:
						MessageSetting = True
						while(MessageSetting): 
							print("Welcome to Message settings")
	
							message = """
							press a number:
	
							1: Set 1
							2: Common
							0: Return
	
							"""
							print(message)
							select = int(input())
	
							match(select):
								case 1:
									Set1 = True
									while(Set1): 
										print("Welcome to Set 1")
	
										message = """
										press a number:
	
										1: Message centre number
										2: Message sent as
										3: Message validity
										0: Return to MessageSettings
	
										"""
										print(message)
										select = int(input())
	
										match(select):
	
											case 1:
												MessageCentre = True
												while(MessageCentre): 
													print("Welcome to MessageCentre")
													message = """
													press a number:
	
													0: Return to Set 1
	
													"""
													print(message)
													selectPhonebook = int(input())
	
													match(selectPhonebook):
														case 0: MessageCentre = False
	
	
														case _: print("Invalid - Try again")
	
	
	
	
											case 2:
												SentAs = True
												while(SentAs): 
													print("Welcome to SentAs")
													message = """
													press a number:
	
													0: Return to Set 1
	
													"""
													print(message)
													selectPhonebook = int(input())
	
													match(selectPhonebook):
														case 0: SentAs = False
	
	
														case _: print("Invalid - Try again")
	
	
	
											case 3:
												MessageValidity = True
												while(MessageValidity): 
													print("Welcome to MessageValidity")
													message = """
													press a number:
	
													0: Return to Set 1
	
													"""
													print(message)
													selectPhonebook = int(input())
	
													match(selectPhonebook):
														case 0: MessageValidity = False
	
	
														case _: print("Invalid - Try again")
	
	
											case 0: Set1 = False
	
	
	
	
	
											case _: print("Invalid - Try again")
	
	
								case 2:
									Common = True
									while(Common): 
										print("Welcome to Common")
	
										message = """
										press a number:
	
										1: Delivery report
										2: Reply via same centre
										3: Character support
										0: Return to MessageSettings
	
										"""
										print(message)
										select = int(input())
	
										match(select):
	
											case 1:
												DeliveryReport = True
												while(DeliveryReport): 
													print("Welcome to DeliveryReport")
													message = """
													press a number:
	
													0: Return to Common
	
													"""
													print(message);
													selectPhonebook = int(input())
	
													match(selectPhonebook):
														case 0: DeliveryReport = False
	
	
														case _: print("Invalid - Try again")
	
	
											case 2:
												ReplyViaCentre = True
												while(ReplyViaCentre): 
													print("Welcome to Reply Via Centre")
													message = """
													press a number:
	
													0: Return to Common
	
													"""
													print(message)
													selectPhonebook = int(input())
	
													match(selectPhonebook):
														case 0: ReplyViaCentre = False
	
	
														case _: print("Invalid - Try again")
	
	
	
											case 3:
												CharacterSupport = True
												while(CharacterSupport): 
													print("Welcome to Character Support")
													message = """
													press a number:
	
													0: Return to Common
	
													"""
													print(message)
													selectPhonebook = int(input())
	
													match(selectPhonebook):
														case 0: CharacterSupport = False
	
	
														case _: print("Invalid - Try again")
	
	
	
											case 0:
												Common = False
	
											case _: print("Invalid - Try again")
	
								case 0:
									MessageSetting = False
	
								case _: print("Invalid - Try again")
	
	
	
	
	
	
					case 8:
						InfoService = True
						while(InfoService): 
							print("Welcome to InfoService")
							message = """
							press a number:
	
							0: Return to Messages
	
							"""
							print(message)
							selectPhonebook = int(input())
	
							match(selectPhonebook):
								case 0: InfoService = False
	
								case _: print("Invalid - Try again")
	
	
	
					case 9:
						VoiceMailBoxMessage = True
						while(VoiceMailBoxMessage): 
							print("Welcome to Voice Mail Box Message")
							message = """
							press a number:
	
							0: Return to Messages
	
							"""
							print(message)
							selectPhonebook = int(input())
							match(selectPhonebook):
								case 0: VoiceMailBoxMessage = False
	
								case _: print("Invalid - Try again")
	
	
	
					case 10:
						Servicecommandeditor = True
						while(Servicecommandeditor): 
							print("Welcome to Service command editor")
							message = """
							press a number:
	
							0: Return to Messages
	
							"""
							print(message)
							selectPhonebook = int(input())
	
							match(selectPhonebook):
								case 0: Servicecommandeditor = False
	
	
								case _: print("Invalid - Try again")
	
	
	
					case 0:
						Messages = False
	
					case _: print("Who you be???... Do am again");
	
	
	

		case 3:
			Chat = True
			while(Chat): 
				print("Welcome to Chat");
				message = """
				press a number:

				0: Return to Menu

				"""
				print(message)
				selectPhonebook = int(input())

				match(selectPhonebook):
					case 0: Chat = False


					case _: print("Invalid - Try again");





		case 4:
			Callregister = True
			while(Callregister): 
				print("Welcome to Call register");
				
				message = """
				press a number:
				
				1: Missed calls
				2: Recieving calls
				3: Dialled numbers
				4: Erase recent call lists
				5: Show call duration
				6: Show call costs
				7: call cost settings
				8: Prepaid credit
				0: return to the menu
				"""
				print(message)
				select = int(input())
				
				match(select):
				
					case 1:
						MissedCall = True
						while(MissedCall): 
							print("Welcome to Missed Call")
							message = """
							press a number:
				
							0: Return to Call register
				
							"""
							print(message)
							selectPhonebook = int(input())
				
							match(selectPhonebook):
								case 0: MissedCall = False
				
				
								case _: print("Invalid - Try again")
				
				
					case 2:
						ReceivingCall = True
						while(ReceivingCall):  
							print("Welcome to Receiving call")
							message = """
							press a number:
				
							0: Return to Call register
				
							"""
							print(message);
							selectPhonebook = int(input())
				
							match(selectPhonebook):
								case 0: ReceivingCall = False
				
				
								case _: print("Invalid - Try again");
				
				
					case 3:
						DialledNumber = True
						while(DialledNumber):  
							print("Welcome to Dialled Number")
							message = """
							press a number:
				
							0: Return to Call register
				
							"""
							print(message)
							selectPhonebook = int(input())
				
							match(selectPhonebook):
								case 0: DialledNumber = False
				
				
								case _: print("Invalid - Try again")
				
				
					case 4:
						EraseRecentCallList = True
						while(EraseRecentCallList):    
							print("Welcome to Erase Recent Call List")
							message = """
							press a number:
				
							0: Return to Call register
				
							"""
							print(message)
							selectPhonebook = int(input())
				
							match(selectPhonebook):
								case 0: EraseRecentCallList = False
				
				
								case _: print("Invalid - Try again")
				
				
					case 5:
						callduration = True
						while(callduration): 
							print("Welcome to show call duration")
				
							message = """
							press a number:
				
							1: Last call duration
							2: All calls' duration
							3: Received calls' duration
							4: Dialled calls' duration
							5: Clear timers
							0: return to call register
							"""
							print(message)
							select = int(input())
				
							match(select):
								case 1:
									Lastcallduration = True
									while(Lastcallduration): 
										print("Welcome to Last call duration")
										message = """
										press a number:
				
										0: Return to Call Duration
				
										"""
										print(message)
										selectPhonebook = int(input())
				
										match(selectPhonebook):
											case 0: Lastcallduration = False
				
				
											case _: print("Invalid - Try again")
				
				
				
								case 2:
									AllCallDuration = True
									while(AllCallDuration): 
										print("Welcome to All Call Duration")
										message = """
										press a number:
				
										0: Return to Call Duration
				
										"""
										print(message)
										selectPhonebook = int(input())
				
										match(selectPhonebook):
											case 0: AllCallDuration = False
				
											case _: print("Invalid - Try again")
				
				
				
								case 3:
									ReceivedCallDurations = True
									while(ReceivedCallDurations): 
										print("Welcome to Received Call Durations")
										message = """
										press a number:
				
										0: Return to Call Duration
				
										"""
										print(message)
										selectPhonebook = int(input())
				
										match(selectPhonebook):
											case 0: ReceivedCallDurations = False
			
				
											case _: print("Invalid - Try again")
				
				
				
								case 4:
									DialledCallDurations = True
									while(DialledCallDurations): 
										print("Welcome to Dialled Call Durations")
										message = """
										press a number:
				
										0: Return to Call Duration
				
										"""
										print(message);
										selectPhonebook = int(input())
				
										match(selectPhonebook):
											case 0: DialledCallDurations = False
				
				
											case _: print("Invalid - Try again")
				
				
				
								case 5:
									ClearTimers = true;
									while(ClearTimers): 
										print("Welcome to Clear Timer")
										message = """
										press a number:
				
										0: Return to Call Duration
					
										"""
										print(message)
										selectPhonebook = int(input())
				
										match(selectPhonebook):
											case 0: ClearTimers = False
					
				
											case _: print("Invalid - Try again")
				
				
				
								case 0:
									callduration = False
				
								case _: print("Who you be???... Do am again")
				
				
				
				
				
					case 6:
						Showcallcost = True
						while(Showcallcost): 
							print("Welcome to Show call costs")
				
							message = """
							press a number:
				
							1: Last call cost
							2: All calls' cost
							3: Clear counters
							0: return to Call register
							"""
							print(message)
							select = int(input())
				
							match(select):
								case 1:
									Lastcallcost = True
									while(Lastcallcost): 
										print("Welcome to Last call cost")
										message = """
										press a number:
				
										0: Return to Show call cost
				
										"""
										print(message)
										selectPhonebook = int(input())
				
										match(selectPhonebook):
											case 0: Lastcallcost = False
				
				
											case _: print("Invalid - Try again")
				
				
				
								case 2:
									Allcallcost = True
									while(Allcallcost): 
										print("Welcome to All call cost")
										message = """
										press a number:
				
										0: Return to Show call cost
				
										"""
										print(message);
										selectPhonebook = int(input())
				
										match(selectPhonebook):
											case 0: Allcallcost = False
			
				
											case _: print("Invalid - Try again")
				
			
				
								case 3:
									Clearcounter = True
									while(Clearcounter): 
										print("Welcome to Clear counter")
										message = """
										press a number:
				
										0: Return to Show call cost
				
										"""
										print(message)
										selectPhonebook = int(input())
				
										match(selectPhonebook):
											case 0: Clearcounter = False
				
				
											case _: print("Invalid - Try again")
				
				
				
				
								case 0:
									Showcallcost = False
				
								case _: print("Who you be???... Do am again")
				
				
				
				
				
				
					case 7:
						Callcostsettings = True
						while(Callcostsettings): 
							print("Welcome to call cost settings")
				
							message = """
							press a number:
				
							1: Call cost limit
							2: Show costs in
							0: return to Call cost settings
							"""
							print(message);
							select = int(input())
				
							match(select):
								case 1:
									Callcostlimit = True
									while(Callcostlimit): 
										print("Welcome to Call cost limit")
										message = """
										press a number:
				
										0: Return to call cost settings
					
										"""
										print(message)
										selectPhonebook = int(input())
				
										match(selectPhonebook):
											case 0: Callcostlimit = False
				
				
											case _: print("Invalid - Try again")
				
				
				
								case 2:
									CostIn = True
									while(CostIn): 
										print("Welcome to Cost in")
										message = """
										press a number:
				
										0: Return to call cost settings
				
										"""
										print(message)
										selectPhonebook = int(input())
				
										match(selectPhonebook):
											case 0: CostIn = False
			
				
											case _: print("Invalid - Try again")
				
				
				
				
								case 0:
									Callcostsettings = False
				
								case _: print("Who you be???... Do am again")
				
				
				
				
				
				
					case 8:
						PrepaidCredit = True
						while(PrepaidCredit): 
							print("Welcome to Prepaid Credit")
							message = """
							press a number:
				
							0: Return to Call register
				
							"""
							print(message)
							selectPhonebook = int(input())
				
							match(selectPhonebook):
								case 0: PrepaidCredit = False
				
				
								case _: print("Invalid - Try again")
				
				
				
					case 0:
						Callregister = False
				
					case _: print("Who you be???... Do am again")
				
				
				

		case 5:
			Tone = True
			while(Tone): 
				print("Welcome to Tone")
				message = """
				press a number:
			
				1: Ringing tone
				2: Ringing volume
				3: Incoming call alert
				4: Composer
				5: Message alert tone
				6: Keypad tones
				7: Warning and game tones
				8: Viberating alert
				9: Screen saver
				0: Return to menu
				""";
				print(message)
				select = int(input())
			
				match(select):
			
					case 1:
						Ringingtone = True
						while(Ringingtone): 
							print("Ringing tone")
							message = """
							press a number:
			
							0: Return to menu
			
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: Ringingtone = False
			
			
								case _: print("Invalid - Try again")
			
			
			
					case 2:
						RingingVolume = True
						while(RingingVolume): 
							print("Ringing Volume")
							message = """
							press a number:
			
							0: Return to menu
			
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: RingingVolume = False
			
			
								case _: print("Invalid - Try again")
			
			
			
					case 3:
						IncomingCallAlert = True
						while(IncomingCallAlert): 
							print("Incoming Call Alert")
							message = """
							press a number:
			
							0: Return to menu
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: IncomingCallAlert = False
			
			
								case _: print("Invalid - Try again")
			
			
			
					case 4:
						Composer = True
						while(Composer): 
							print("Composer")
							message = """
							press a number:
			
							0: Return to menu
			
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: Composer = False
			
			
								case _: print("Invalid - Try again")
			
			
					case 5:
						MessageAlertTone = True
						while(MessageAlertTone): 
							print("Message Alert Tone")
							message = """
							press a number:
			
							0: Return to menu
			
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: MessageAlertTone = False
					
								case _: print("Invalid - Try again")
			
			
			
			
					case 6:
						KeypadTone = True
						while(KeypadTone): 
							print("Keypad Tone")
							message = """
							press a number:
			
							0: Return to menu
			
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: KeypadTone = False
			
			
								case _: print("Invalid - Try again")
			
			
			
			
					case 7:
						WarningAndGameTone = True
						while(WarningAndGameTone): 
							print("Warning And Game Tone")
							message = """
							press a number:
			
							0: Return to menu
			
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: WarningAndGameTone = False
			
			
								case _: print("Invalid - Try again")
			
			
			
			
					case 8:
						VibratingTone = True
						while(VibratingTone): 
							print("Vibrating Tone")
							message = """
							press a number:
			
							0: Return to menu
			
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: VibratingTone = False
			
			
								case _: print("Invalid - Try again")
			
			
					case 9:
						ScreenSaver = True
						while(ScreenSaver): 
							print("Screen Saver")
							message = """
							press a number:
			
							0: Return to menu
			
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: ScreenSaver = False
				
			
								case _: print("Invalid - Try again")
			
			
			
			
					case 0:
						Tone = False
			
					case _: print("Who you be???... Do am again")
			
			


		case 6:
			Settings = True
			while(Settings): 
			
				print("Welcome to Settings")
			
				message = """
				press a number:
			
				1: Call Settings
				2: Phone settings
				3: Security settings
				4: Restore factory settings
				0: Return to menu
			
				"""
				print(message);
				select = int(input())
			
				match(select):
			
					case 1:
						CallSettings = True
						while(CallSettings): 
							print("Call Settings")
			
							message = """
							press a number:
			
							1: Automatic redial
							2: Speed dialing
							3: Call waiting options
							4: Own number sending
							5: Phone line in use
							6: Automatic answer
							0: return to Settings
							"""
							print(message)
							select = int(input())
			
							match(select):
			
								case 1:
									AutomaticRedial = True
									while(AutomaticRedial): 
										print("Welcome to automatic redial")
										message = """
										press a number:
			
										0: Return to call settings
			
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: AutomaticRedial = False
			
			
											case _: print("Invalid - Try again")
			
			
			
								case 2:
									Speeddialling = True
									while(Speeddialling): 
										print("Welcome to Speed dialling")
										message = """
										press a number:
			
										0: Return to call settings
			
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: Speeddialling = False
			
			
											case _: print("Invalid - Try again")
			
			
			
								case 3:
									Callwaitingoption = True
									while(Callwaitingoption): 
										print("Welcome to Call waiting option")
										message = """
										press a number:
			
										0: Return to call settings
			
										"""
										print(message);
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: Callwaitingoption = False
			
			
											case _: print("Invalid - Try again")
			
			
			
								case 4:
									Ownnumbersending = True
									while(Ownnumbersending): 
										print("Welcome to Own number sending")
										message = """
										press a number:
			
										0: Return to call settings
			
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: Ownnumbersending = False
			
			
											case _: print("Invalid - Try again")
			
			
			
								case 5:
									Phonelineinuse = True
									while(Phonelineinuse): 
										print("Welcome to Phone line in use")
										message = """
										press a number:
			
										0: Return to call settings
			
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: Phonelineinuse = False
			
			
											case _: print("Invalid - Try again")			
			
			
								case 6:
									AutomaticAnswer = True
									while(AutomaticAnswer): 
										print("Welcome to Automatic Answer")
										message = """
										press a number:
			
										0: Return to call settings
			
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: AutomaticAnswer = False
		
			
											case _: print("Invalid - Try again")
			
					
			
			
								case 0:
									CallSettings = False
			
								case _: print("Who you be???... Do am again")
			
			
			
			
			
			
					case 2:
						PhoneSettings = True
						while(PhoneSettings): 
							print("Phone settings")
			
							message = """
							press a number:
			
							1: Language
							2: Cell info display
							3: Welcome note
							4: Network selection
							5: Lights
							6: Confirm SIM service action
							0: return to settings
							"""
							print(message)
							select = int(input())
			
							match(select):
			
								case 1:
									Language = True
									while(Language): 
										print("Welcome to Language")
										message = """
										press a number:
			
										0: Return to phone settings
			
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: Language = False
			
			
											case _: print("Invalid - Try again")
			
			
			
								case 2:
									CellinfoDisplay = True
									while(CellinfoDisplay): 
										print("Welcome to Cell info Display")
										message = """
										press a number:
			
										0: Return to phone settings
			
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: CellinfoDisplay = False
			
			
											case _: print("Invalid - Try again")
			
			
			
								case 3:
									WelcomeNote = True
									while(WelcomeNote): 
										print("Welcome to Welcome Note")
										message = """
										press a number:
			
										0: Return to phone settings
			
										"""
										print(message);
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: WelcomeNote = false;
			
			
											case _: print("Invalid - Try again")
			
			
			
								case 4:
									NetworkSelection = True
									while(NetworkSelection): 
										print("Welcome to Network Selection")
										message = """
										press a number:
			
										0: Return to phone settings
			
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: NetworkSelection = False
			
			
											case _: print("Invalid - Try again")
			
			
			
								case 5:
									Lights = True
									while(Lights): 
										print("Welcome to Lights")
										message = """
										press a number:
			
										0: Return to phone settings
			
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: Lights = False
			
			
											case _: print("Invalid - Try again")
			
			
			
								case 6:
									SimServiceAction = True
									while(SimServiceAction): 
										print("Welcome to Confirm Sim Service Action")
										message = """
										press a number:
			
										0: Return to phone settings
			
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: SimServiceAction = False
		
			
											case _: print("Invalid - Try again")
			
			
			
			
								case 0:
									PhoneSettings = False
				
								case _: print("Who you be???... Do am again")
			
			
			
			
			
			
					case 3:
						SecuritySettings = True
						while(SecuritySettings): 
							print("Security settings")
			
							message = """
							press a number:
			
							1: PIN code request
							2: Call barring service
							3: Fixed dialling
							4: Closed user group
							5: Phone security
							6: Change access codes
							0: return to settings
							"""
							print(message)
							select = int(input())
			
							match(select):
			
								case 1:
									Pincoderequest = True
									while(Pincoderequest): 
										print("Welcome to Pin code request")
										message = """
										press a number:
			
										0: Return to Security settings
			
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: Pincoderequest = False
							
			
											case _: print("Invalid - Try again")
			
			
								case 2:
									Callbarringservice = True
									while(Callbarringservice): 
										print("Welcome to Call barring service")
										message = """
										press a number:
			
										0: Return to Security settings
			
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: Callbarringservice = False
			
			
											case _: print("Invalid - Try again")
			
			
			
								case 3:
									Fixeddialling = True
									while(Fixeddialling): 
										print("Welcome to Fixed dialling")
										message = """
										press a number:
			
										0: Return to Security settings
			
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: Fixeddialling = False
				
			
											case _: print("Invalid - Try again")
			
			
			
								case 4:
									ClosedUserGroup = True
									while(ClosedUserGroup): 
										print("Welcome to Closed User Group")
										message = """
										press a number:
			
										0: Return to Security settings
			
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: ClosedUserGroup = False
			
			
											case _: print("Invalid - Try again")
			
			
			
								case 5:
									Phonesecurity = True
									while(Phonesecurity): 
										print("Welcome to Phone security")
										message = """
										press a number:
			
										0: Return to Security settings
			
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: Phonesecurity = False
			
			
											case _: print("Invalid - Try again")
			
			
			
								case 6:
									ChangeAccessCode = True
									while(ChangeAccessCode): 
										print("Welcome Change Access Code")
										message = """
										press a number:
			
										0: Return to Security settings
			
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: ChangeAccessCode = False
			
			
											case _: print("Invalid - Try again")
			
			
			
			
								case 0:
									SecuritySettings = False
			
								case _: print("Who you be???... Do am again")
			
			
			
			
			
			
					case 4:
						Restorefactorysettings = True
						while(Restorefactorysettings): 
							print("Welcome Restore factory settings")
							message = """
							press a number:
			
							0: Return to settings
			
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: Restorefactorysettings = False
			
			
								case _: print("Invalid - Try again")			
			
					case 0:
						Settings = False
			
					case _: print("Who you be???... Do am again")
			


		case 7:
			CallDivert = True
			while(CallDivert): 
				print("Welcome to Call Divert")
				message = """
				press a number:
			
				0: Return to CallDivert
			
				"""
				print(message);
				selectPhonebook = int(input())
			
				match(selectPhonebook):
					case 0: CallDivert = False
			
			
					case _: print("Invalid - Try again")
			


		case 8:
			Games = True
			while(Games): 
				print("Welcome to Games")
				message = """
				press a number:
			
				0: Return to Games
			
				"""
				print(message);
				selectPhonebook = int(input())
			
				match(selectPhonebook):
					case 0: Games = False
			
			
					case _: print("Invalid - Try again")
			


		case 9:
			Calculator = True
			while(Calculator): 
				print("Welcome to Calculator")
				message = """
				press a number:
			
				0: Return to Calculator
			
				"""
				print(message)
				selectPhonebook = int(input())
			
				match(selectPhonebook):
					case 0: Calculator = False
			
			
					case _: print("Invalid - Try again")
			


		case 10:
			Remainders = True
			while(Remainders): 
				print("Welcome to Remainders")
				message = """
				press a number:
			
				0: Return to Remainders
			
				"""
				print(message);
				selectPhonebook = int(input())
			
				match(selectPhonebook):
					case 0: Remainders = False
			
			
					case _: print("Invalid - Try again")
			


		case 11:
			Clock = True
			while(Clock): 
				print("Welcome to Clock")
			
				message = """
				press a number:
			
				1: Alarm clock
				2: Clock settings
				3: Date settings
				4: Stopwatch
				5: Countdown timer
				6: Auto update of date and time
				0: Go back
				"""
				print(message)
				select = int(input())
			
				match(select):
			
					case 1:
						AlarmClock = True
						while(AlarmClock): 
							print("Welcome to AlarmClock")
							message = """
							press a number:
			
							0: Return to Clock
			
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: AlarmClock = False
			
			
								case _: print("Invalid - Try again")
			
			
			
					case 2:
						ClockSetting = True
						while(ClockSetting): 
							print("Welcome to ClockSetting")
							message = """
							press a number:
			
							0: Return to Clock
			
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: ClockSetting = False
			
			
								case _: print("Invalid - Try again")
			
			
			
					case 3:
						Datesettings = True
						while(Datesettings): 
							print("Welcome to Date settings")
							message = """
							press a number:
			
							0: Return to Clock
			
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: Datesettings = False
		
			
								case _: print("Invalid - Try again")
			
			
			
					case 4:
						StopWatch = True
						while(StopWatch): 
							print("Welcome to Stop Watch")
							message = """
							press a number:
			
							0: Return to Clock
			
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: StopWatch = false;
			
			
								case _: print("Invalid - Try again")
			
			
			
					case 5:
						CountdownTimer = True
						while(CountdownTimer): 
							print("Welcome to Countdown Timer")
							message = """
							press a number:
			
							0: Return to Clock
			
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: CountdownTimer = False
			
			
								case _: print("Invalid - Try again")
			
			
			
					case 6:
						Autoupdateoftimeanddate = True
						while(Autoupdateoftimeanddate): 
							print("Welcome to Autoupdateoftimeanddate")
							message = """
							press a number:
			
							0: Return to Clock
			
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: Autoupdateoftimeanddate = False
		
			
								case _: System.out.println("Invalid - Try again")
			
			
			
					case 0:
						Clock = False
			
					case _: print("Who you be???... Do am again")
	
			


		case 12:
			Profile = True
			while(Profile): 
				print("Welcome to Remainders")
				message = """
				press a number:
			
				0: Return to Profile
			
				"""
				print(message);
				selectPhonebook = int(input())
			
				match(selectPhonebook):
					case 0: Profile = False
			
			
					case _: print("Invalid - Try again")
			


		case 13:
			SimService = True
			while(SimService): 
				print("Welcome to Remainders")
				message = """
				press a number:
			
				0: Return to SimService
			
				"""
				print(message)
				selectPhonebook = int(input())
			
				match(selectPhonebook):
					case 0: SimService = False
			
			
					case _: print("Invalid - Try again")
			



		
		case 0: menu = False
			
		
		
		case _: print("Calm down na... Do am again")
