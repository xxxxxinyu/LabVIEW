<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="23008000">
	<Property Name="NI.LV.All.SourceOnly" Type="Bool">true</Property>
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="data" Type="Folder">
			<Item Name="combined_wordlist.txt" Type="Document" URL="../data/combined_wordlist.txt"/>
			<Item Name="common_words.txt" Type="Document" URL="../data/common_words.txt"/>
			<Item Name="fail.wav" Type="Document" URL="../data/fail.wav"/>
			<Item Name="precalculated_guesses.npz" Type="Document" URL="../data/precalculated_guesses.npz"/>
			<Item Name="success.wav" Type="Document" URL="../data/success.wav"/>
		</Item>
		<Item Name="python" Type="Folder">
			<Item Name="__pycache__" Type="Folder">
				<Item Name="isLegal.cpython-39.pyc" Type="Document" URL="../python/__pycache__/isLegal.cpython-39.pyc"/>
				<Item Name="LetterInformation.cpython-39.pyc" Type="Document" URL="../python/__pycache__/LetterInformation.cpython-39.pyc"/>
				<Item Name="LetterInformation.cpython-310.pyc" Type="Document" URL="../python/__pycache__/LetterInformation.cpython-310.pyc"/>
				<Item Name="OutcomeBasedAI.cpython-39.pyc" Type="Document" URL="../python/__pycache__/OutcomeBasedAI.cpython-39.pyc"/>
				<Item Name="OutcomeBasedAI.cpython-310.pyc" Type="Document" URL="../python/__pycache__/OutcomeBasedAI.cpython-310.pyc"/>
				<Item Name="play.cpython-39.pyc" Type="Document" URL="../python/__pycache__/play.cpython-39.pyc"/>
				<Item Name="randomAns.cpython-39.pyc" Type="Document" URL="../python/__pycache__/randomAns.cpython-39.pyc"/>
				<Item Name="randomAns.cpython-310.pyc" Type="Document" URL="../python/__pycache__/randomAns.cpython-310.pyc"/>
				<Item Name="WordleJudge.cpython-39.pyc" Type="Document" URL="../python/__pycache__/WordleJudge.cpython-39.pyc"/>
				<Item Name="WordleJudge.cpython-310.pyc" Type="Document" URL="../python/__pycache__/WordleJudge.cpython-310.pyc"/>
			</Item>
			<Item Name="isLegal.py" Type="Document" URL="../python/isLegal.py"/>
			<Item Name="LetterInformation.py" Type="Document" URL="../python/LetterInformation.py"/>
			<Item Name="OutcomeBasedAI.py" Type="Document" URL="../python/OutcomeBasedAI.py"/>
			<Item Name="play.py" Type="Document" URL="../python/play.py"/>
			<Item Name="randomAns.py" Type="Document" URL="../python/randomAns.py"/>
			<Item Name="WordleJudge.py" Type="Document" URL="../python/WordleJudge.py"/>
		</Item>
		<Item Name="SubVIs" Type="Folder">
			<Item Name="change_color.vi" Type="VI" URL="../wordle_SubVI.llb/change_color.vi"/>
			<Item Name="change_color0103.vi" Type="VI" URL="../wordle_SubVI.llb/change_color0103.vi"/>
			<Item Name="end.vi" Type="VI" URL="../wordle_SubVI.llb/end.vi"/>
			<Item Name="get_location.vi" Type="VI" URL="../wordle_SubVI.llb/get_location.vi"/>
			<Item Name="get_location0103.vi" Type="VI" URL="../wordle_SubVI.llb/get_location0103.vi"/>
			<Item Name="get_signal.vi" Type="VI" URL="../wordle_SubVI.llb/get_signal.vi"/>
			<Item Name="initialize.vi" Type="VI" URL="../wordle_SubVI.llb/initialize.vi"/>
			<Item Name="wordle_SubVI.llb" Type="Document" URL="../wordle_SubVI.llb"/>
		</Item>
		<Item Name="main.vi" Type="VI" URL="../main.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="_2DArrToArrWfms.vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/_2DArrToArrWfms.vi"/>
				<Item Name="_ArrWfmsTo1DInterleave.vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/_ArrWfmsTo1DInterleave.vi"/>
				<Item Name="_ArrWfmsTo2DArr.vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/_ArrWfmsTo2DArr.vi"/>
				<Item Name="_ArrWfmsToData.vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/_ArrWfmsToData.vi"/>
				<Item Name="_Get Sound Error From Return Value.vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/_Get Sound Error From Return Value.vi"/>
				<Item Name="Path To Command Line String.vi" Type="VI" URL="/&lt;vilib&gt;/AdvancedString/Path To Command Line String.vi"/>
				<Item Name="PathToUNIXPathString.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/CFURL.llb/PathToUNIXPathString.vi"/>
				<Item Name="Play Sound File.vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Play Sound File.vi"/>
				<Item Name="Sampling Mode.ctl" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sampling Mode.ctl"/>
				<Item Name="Sound Data Format.ctl" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound Data Format.ctl"/>
				<Item Name="Sound File Close.vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound File Close.vi"/>
				<Item Name="Sound File Info (path).vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound File Info (path).vi"/>
				<Item Name="Sound File Info (refnum).vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound File Info (refnum).vi"/>
				<Item Name="Sound File Info.vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound File Info.vi"/>
				<Item Name="Sound File Open.vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound File Open.vi"/>
				<Item Name="Sound File Position.ctl" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound File Position.ctl"/>
				<Item Name="Sound File Read (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound File Read (DBL).vi"/>
				<Item Name="Sound File Read (I16).vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound File Read (I16).vi"/>
				<Item Name="Sound File Read (I32).vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound File Read (I32).vi"/>
				<Item Name="Sound File Read (SGL).vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound File Read (SGL).vi"/>
				<Item Name="Sound File Read (U8).vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound File Read (U8).vi"/>
				<Item Name="Sound File Read Open.vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound File Read Open.vi"/>
				<Item Name="Sound File Read.vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound File Read.vi"/>
				<Item Name="Sound File Refnum.ctl" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound File Refnum.ctl"/>
				<Item Name="Sound File Write Open.vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound File Write Open.vi"/>
				<Item Name="Sound Output Configure.vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound Output Configure.vi"/>
				<Item Name="Sound Output Task ID.ctl" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound Output Task ID.ctl"/>
				<Item Name="Sound Output Wait.vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound Output Wait.vi"/>
				<Item Name="Sound Output Write (DBL Single).vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound Output Write (DBL Single).vi"/>
				<Item Name="Sound Output Write (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound Output Write (DBL).vi"/>
				<Item Name="Sound Output Write (I16).vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound Output Write (I16).vi"/>
				<Item Name="Sound Output Write (I32).vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound Output Write (I32).vi"/>
				<Item Name="Sound Output Write (SGL).vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound Output Write (SGL).vi"/>
				<Item Name="Sound Output Write (U8).vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound Output Write (U8).vi"/>
				<Item Name="Sound Output Write.vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound Output Write.vi"/>
				<Item Name="Space Constant.vi" Type="VI" URL="/&lt;vilib&gt;/dlg_ctls.llb/Space Constant.vi"/>
			</Item>
			<Item Name="lvsound2.dll" Type="Document" URL="/&lt;resource&gt;/lvsound2.dll"/>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
