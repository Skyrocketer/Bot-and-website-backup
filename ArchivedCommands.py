#poll command
'''
@bot.command(brief='A voting/poll command, STILL UNDER DEV', description='Use this to make a poll or vote, STILL UNDER DEV', aliases=['vote'])
@commands.has_any_role('moderator')
async def poll(ctx, question, option1, option2):
    #try:
        print('>NEW POLL CREATED: '+question+', CREATED BY: '+str(ctx.author)+' WITH THE OPTIONS '+option1+' '+option2)
        await ctx.message.delete()
        poleselect = await ctx.send(str(ctx.author)+' poll:\n'+question+':\n*(use "#ENDPOLE" to end this poll)*', components=[Select(placeholder='Select a option', options=[SelectOption(label=option1, value='option1'), SelectOption(label=option2, value='option2')], custom_id=question)])
        vote1 = "0"
        vote2 = "0"
        message = await ctx.send('**VOTING: \n__'+option1+':__ '+vote1+' \n__'+option2+':__ '+vote2+'**', components=[Button(label='End poll/vote', custom_id=question, style=int(3))])
        voted = []
        while True:
          select, message = [await bot.wait_for('select_option'), await bot.wait_for('message')]
          if select.component.custom_id == question:
            if select.author.id in voted:
              await select.send(content='You already voted!')
            else:
              selected = select.values[0]
              if selected == 'option1':
                await select.send(content="You voted for: "+option1)
                print('>'+question+' POLL LOG: '+str(select.author)+' voted for '+option1)
              else:
                await select.send(content="You voted for "+option2)
                print('>'+question+' POLL LOG: '+str(select.author)+' voted for '+option2)
              voted.append(select.author.id)
              if select.values[0] == 'option1':
                vote1 = int(vote1)
                vote1 = vote1 + 1
                vote1 = str(vote1)
                await message.edit(content='**VOTING: \n__'+option1+':__ '+vote1+'** \n**__'+option2+':__ '+vote2+'**')
              elif select.values[0] == 'option2':
                vote2 = int(vote2)
                vote2 = vote2 + 1
                vote2 = str(vote2)
                await message.edit(content='**VOTING: \n__'+option1+':__ '+vote1+'** \n**__'+option2+':__ '+vote2+'**')
          elif message.content == '#ENDPOLE':
              if message.author.id == ctx.author.id:
                await poleselect.delete()
                await message.delete()
                win = ''
                winvotes = ''
                if vote1 > vote2:
                  win = option1
                  winvotes = str(vote1)
                  await message.send(content='Pole ended and '+win+' won with '+winvotes+'!', ephemeral=False)
                elif vote2 > vote1:
                  win = option2
                  winvotes = str(vote2)
                  await message.send(content='Pole ended and '+win+' won with '+winvotes+'!', ephemeral=False)
                else:
                  win = 'Tie'
                  await message.send(content='Pole ended and a '+win+' happened so nither '+option1+' or '+option2+' won!', ephemeral=False)
                break
              continue
    #except:
      #await ctx.send('Sorry, but an error occoured in my code. Please try again')
'''