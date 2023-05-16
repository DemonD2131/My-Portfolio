import org.code.theater.*;
import java.util.ArrayList;
import java.util.HashSet;
public class ZeldaScene extends Scene{



  String[] keyMap = {"c","C","d","D","e","f","F","g","G","a","A","b", "-", "-", "-"};
  String[] images;
  public ZeldaScene(String[] images){
     this.images = images;
  }

  private String[] stripSong(String[] song){
    String[] temp = new String[song.length];
    for(int num = 0; num < song.length; num++){
      temp[num] = song[num].replace("|", "");
      //temp[num] = song[num].replace(" ", "");
      //temp[num] = song[num].replace("\n", "");
    }
    return temp;
  }
  public String[] generateRandomSong(int length){
/*Takes in a verse numbers of verses as the length
Generates a song, randomly, random number of notes simultaneously, and has a 1 in 15 chance to be any note and a 3 in 15 chance to be a rest note


*/
    String verse;
    String[] song = new String[length];
    
    for( int i = 0; i < length; i++){
      verse = "";
      int multinotes = (int)(Math.random() * 8)+1;
      for(int j = 0; j < multinotes; j ++){
        verse += Integer.toString((int)(Math.random() * 3) + 3);
        for(int e = 0; e < 26; e++){
          verse += keyMap[(int)(Math.random() * 15)];
        }
      }
      song[i] = verse;
    }
    return song;
  }
  
  public String[] adjustSongRandomly(String[] song, int randomness){
    //Takes the song, have a 1 in randomness(variable) chance to change the note to one of the notes in the keyMap[]
    
    song = stripSong(song);
    int maxStringLength = 0;
    for(String str : song){
      if(str.length() > maxStringLength){
        maxStringLength = str.length();
      }
    }
    char[][] charArray = new char[song.length][maxStringLength];
    int choosechange = 0;

    for(int i = 0; i < song.length; i++){
      
      charArray[i] = song[i].toCharArray();
      for(int j = 0; j < song[i].length(); j++){
        if(Character.getNumericValue(charArray[i][j]) != 2 && Character.getNumericValue(charArray[i][j]) != 3 && Character.getNumericValue(charArray[i][j]) != 4 && Character.getNumericValue(charArray[i][j]) != 5 && Character.getNumericValue(charArray[i][j]) != 6){
          choosechange = (int)(Math.random() *randomness);
          if(choosechange == 0){
            //System.out.println(keyMap[(int)(Math.random() * 15)].toCharArray()[0]);
            charArray[i][j] = keyMap[(int)(Math.random() * 15)].toCharArray()[0];
          }
        }
      }
      song[i] = String.valueOf(charArray[i]);
    }
    
    return song;
  }
  public ArrayList<ArrayList<Integer>> convertSheetMusic(String[] song){
    //format is as such 5|----------------------e-d-|
    //len of each row is 29
    //we are not using csv so new format is 5|----------------------e-d-|4|f-a-b---f-a-b---f-a-b-----|
    //the format uses the length of the strings which is 26 for each verse, seperated by array 
    //the number at the beginning is the octave
    //the - is a pause
    //each note is aproximately 0.14 seconds (for sarias song at least) edit: a lot of songs are faster than this and the limit is 0.1 :(
    //our keys are all in octave 3, 4, 5, and only c in octave 6
    //we can ignore all |
    
    ArrayList<ArrayList<Integer> > notes = new ArrayList<ArrayList<Integer>>();
    String[] maptemp = {"3c","3C","3d","3D", "3e","3f","3F","3g","3G","3a","3A","3b","4c","4C","4d","4D","4e","4f","4F","4g","4G","4a","4A","4b","5c","5C","5d","5D","5e","5f","5F","5g","5G","5a","5A","5b","6c"};
    ArrayList<String> map = new ArrayList<String>();
    for(String str : maptemp){
      map.add(str);
    }
    //Something to note. I initially did not know that I needed to use an arraylist so thats why we're wasting a bit of memory making a temp array first
    
    //strip the song of unnecesary values
    
    song = stripSong(song);

    //3 layered for loop. Hooray for complicated logic!
    int tempint;
    String tempStr;
    for(int i = 0; i < song.length; i++){
      //includes each verse
      
      for(int j = 0; j < song[i].length(); j += 27){
        //gets a value at the start of each line of notes. if we have just one note happening simultaenously this happens only once
        if(notes.size() < song.length){
          notes.add(new ArrayList<Integer>());
          
        }
        //gets the octave in variable tempint 
        tempint = Integer.parseInt(song[i].substring(j, j+1));
        
        for(int e = j+1; e < j+27; e++){
          //moves through each note, if we run through the prior array multiple times we can get each note to play simultaneously in the same verse

          
//get the note value by taking the octave, the letter, concatenate it together, find the corresponding value in the map arraylist, get the index and add 48
          tempStr = String.valueOf(tempint) + song[i].charAt(e);
          //System.out.print(song[i].charAt(e));
          notes.get(i).add(map.indexOf(tempStr) + 48);

        }
        
      }
    }
    /*
    for(int i = 0; i < notes.size(); i++){
      System.out.print("[");
      for( int j = 0; j < notes.get(i).size(); j++){
        System.out.print(notes.get(i).get(j) + " ");
      }
      System.out.print("]\n");
      
    }
    */
    return notes;
  }
  public void playSong(ArrayList<ArrayList<Integer>> notes, double tempo){
    /*
This inputs a 2d arraylist, and a tempo
the tempo is the seconds each note pauses for
the notes are a 2d arraylist
each array contains a number between 47-84
if it is a 47 it doesnt play anything
it again is a triple for loop
    */
    Key keyBoard = new Key(this);
    for(int i = 0; i < notes.size(); i ++){
      if(i >= 46){
        break;
      }
      //loop through each arraylist in the 2d arraylist
      for(int j = 0; j < 26; j ++){
        //loop through each value within the verse
        for(int e = 0; e < notes.get(i).size(); e += 26){
          //if we play multiple notes, the length will be longer and thus we loop by that and add our position in that loop with a multiple of 26
        if(notes.get(i).get(e + j) >= 48){
        playNote(Instrument.PIANO, notes.get(i).get(e + j), 1.5);
        keyBoard.createKey(notes.get(i).get(e + j), true);
          //play the note for 1.5 seconds. 1.5 is chosen arbitrarily so the note doesnt end abruptly
          //this happens multiple time without pausing if it loops the e variable multiple times
        }
        }
        //pause for each note
        pause(tempo);
        clear("white");
        keyBoard.createBackground();
      
      }
      
    }
  }

  public void createScene(String[] song, double tempo){
    Key baseKeyBoard = new Key(this);
    
    playSong(convertSheetMusic(song), tempo);
    baseKeyBoard.createBackground();
    
  }
}