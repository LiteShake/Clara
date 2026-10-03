
#region IMPORTS
import os
import sys

from Clara.Clara import Clara
from dotenv import load_dotenv
#endregion

#region INIT SETUP
sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(__file__),
        'src'
    )
)

load_dotenv()
TOKEN:str = os.getenv("DISCORD_KEY")
#endregion

#region AWAKE

def Awake( args : list ) -> None :
    
    pass

#endregion

#region START

def Start( args : list ) -> None :
    
    global TOKEN
    
    if( len(args) < 2 ) :
        print("Please specify launch mode")
        return 
    
    match( args[1] ) :
        
        case "bot" :
            
            from Clara.DiscordAPI.Bot import ClaraBot
            
            bot : ClaraBot = ClaraBot( token = TOKEN )
            bot.run( token = TOKEN)
            
        case "daw" :
            return
            
        case "compile" :
            # launchMode : str = "compile"
            
            if(len(args) >= 3) :
                try :
                    Clara.Compile( args[2] )
                except(NotImplementedError) :
                    print("Try again! Compiler not implemented yet")
            else : 
                print("Please add file address to compile!")
            return
            
        case _ :
            print("Unknown Launch mode!")
            pass
    

#endregion

#region ENTRY

if( __name__ == "__main__") :

    arguments:list[str] = sys.argv
    
    Awake( args = arguments )
    Start( args = arguments )    
    
#endregion
