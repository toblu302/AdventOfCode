//infinite loop
+[-
	>>>>>>>>>>-			// Move to c10 set to minus 1
	// While c10 != 0
	[
		[+]++++++++++<<<<<<<<<<		// Set c10 to 10

		//copy cm1 to cm10 uses cm5
			<<<<<<<<<<[-]>>>>>>>>>> // clear cm10
			<
			[-<<<<+>>>>]	// move cm1 to cm5
			<<<<		// move to cm5
			[->>>>+<<<<<<<<<+>>>>>]	// move cm1 to cm1 and cm10
			>>>>>

		//multiply cm1 by ten assumes cm2 cm3 cm4 are 0
			<		// Move to cm1
			[-<+>]		// Move cm1 to cm2
			<<		// Move to cm3
			++++++++++	// Set to 10
			[-		// While cm3 gt 0
				>[-	// While cm2 gt 0
				>+	// inc cm1
				<<<+	// inc cm4
				>>
				]
				<<[->>+<<]	// Move cm4 to cm2
				>
			]
			>>>		// Move to cell 0
			<<[-]>>		// Clear cm2
		

		//handle input and stuff
		,				// Read input to c0
		[->>>>>>>>>>-<<<<<<<<<+<]	// Sub c10 by c0 set c1 to c0
		>[-<<+>>]<			// Add c1 to cm1
		>>++++++++++++++++++++++++++++++++++++++++++++++++	// Set c2 to 48
		[-<<<->>>]	// Sub c2 from cm1
		<<

		.
		>>>>>>>>>>			// Move to c10
	]<<<<<<<<<<

	// stolen division algorithm
	<<<<<<<<<	// Move to cm9
	+++<		// set cm9 to 3
	[>[->+>+<<]>[-<<-[>]>>>[<[-<->]<[>]>>[[-]>>+<]>-<]<<]>>>+<<[-<<+>>]<<<]>>>>>[-<<<<<+>>>>>]<<<<< 

	// subtract 2
	--

	[-<+>]	// add to cm11
	>[-]	// clear cm9
	>>>>>>>>>
	<[-]>	// clear cm1
+]

