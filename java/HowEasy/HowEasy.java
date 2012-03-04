package HowEasy;

public class HowEasy {

	public static final String SEPARATOR_PATTERN = " ";
	public static final String WORD_PATTERN = "(?i)[a-z]+";

	public static final int LEVEL_1 = 250;
	public static final int LEVEL_2 = 500;
	public static final int LEVEL_3 = 1000;

	public void HowEasy() {
		// Do nothing
	}

	protected int getPoints(int awl) {
		if (awl <= 3) {
			return this.LEVEL_1;
		} else if (awl > 3 && awl < 6) {
			return this.LEVEL_2;
		} else {
			return this.LEVEL_3;
		}	
	}

	public int pointVal(String param0) {
		int i;
		int numberOfWords = 0;
		int totalWordsLength = 0;

		String[] stringParts = param0.split(this.SEPARATOR_PATTERN);
		
		for (i=0;i<stringParts.length;i++) {
			if (stringParts[i].matches(this.WORD_PATTERN) ) {
				totalWordsLength += stringParts[i].length();	
				numberOfWords++;
			}
		}

		if (numberOfWords == 0) {
			return this.LEVEL_1;
		} else {
			return this.getPoints(totalWordsLength / numberOfWords);
		}		
	}
}


