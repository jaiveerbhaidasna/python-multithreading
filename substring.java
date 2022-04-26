package termProject;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

public class Substring implements Runnable {
	String base;
	AtomicInteger index;
	String search;
	int start_index;
	
	public Substring(String s, String sub, int startInd) {
		base = s;
		index = new AtomicInteger(-1);
		this.search = sub;
		this.start_index = startInd;

	}

		public int findIndex(String search) {
			int last_index = this.base.length() - search.length() + 1;
			for(int i = 0; i < last_index; i++) {
				int end = i + search.length();
				if(search.equals(base.substring(i, end))) {
					return i;
				}
			}
			return -1;
		}

		public int findIndex_parallel(String search) {
			List<Thread> list = new ArrayList<>();
			int last_index = this.base.length() - search.length() + 1;
			for(int i = 0; i < last_index; i++) {
				Substring s = new Substring(this.base, this.search, i);
				Thread t = new Thread(s);
			
				t.start();
				list.add(t);
			}
			for(Thread t : list) {
				try {
					t.join();
				}
				catch(Exception e) {
					e.printStackTrace();
				}
			}
			
			
			return index.get();
		}
	
	@Override
	public void run() {
		int end = start_index + search.length();
		if(search.equals(base.substring(this.start_index, end)) && start_index < index.get()) {
			boolean flag = false;
			while(!flag)
			{
				flag = index.compareAndSet(index.get(), start_index);
			}
		}
	}
}
