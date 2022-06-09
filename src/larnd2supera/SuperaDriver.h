

#include "EDepSim/TG4Event.h"

namespace larnd2supera {

	class SuperaDriver {
	public:
		SuperaDriver() : val(0) {}

		void ReadEvent(const TG4Event* ev);

	int val;
	};
}
