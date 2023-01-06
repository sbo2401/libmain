JotForm.newDefaultTheme = false;
	JotForm.extendsNewTheme = false;
	JotForm.singleProduct = false;
	JotForm.newPaymentUIForNewCreatedForms = false;
	JotForm.clearFieldOnHide="disable";

	JotForm.init(function(){
	/*INIT-START*/
if (window.JotForm && JotForm.accessible) $('input_64').setAttribute('tabindex',0);
      setTimeout(function() {
          $('input_64').hint('180591001');
       }, 20);
if (window.JotForm && JotForm.accessible) $('input_73').setAttribute('tabindex',0);
if (window.JotForm && JotForm.accessible) $('input_74').setAttribute('tabindex',0);
      JotForm.alterTexts({"confirmClearForm":"Are you sure you want to clear the form","lessThan":"Your score should be less than"});
      setTimeout(function() {
          JotForm.initMultipleUploads();
      }, 2);
	/*INIT-END*/
	});

   JotForm.prepareCalculationsOnTheFly([null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,{"name":"heading","qid":"60","text":"SignUp","type":"control_head"},null,null,null,{"description":"","name":"typeA","qid":"64","subLabel":"","text":"Username","type":"control_textbox"},{"description":"","name":"name","qid":"65","text":"Name","type":"control_fullname"},{"description":"","name":"name66","qid":"66","text":"Name","type":"control_fullname"},{"description":"","name":"email","qid":"67","subLabel":"","text":"Email","type":"control_email"},{"description":"","name":"typeA68","qid":"68","text":"Type a question","type":"control_radio"},null,{"description":"","name":"typeA70","qid":"70","text":"Type a question","type":"control_radio"},null,null,{"description":"","name":"typeA73","qid":"73","subLabel":"","text":"Type a question","type":"control_textbox"},{"description":"","name":"typeA74","qid":"74","subLabel":"","text":"Type a question","type":"control_textbox"},{"description":"","name":"fileUpload","qid":"75","subLabel":"","text":"File Upload","type":"control_fileupload"},{"name":"submit","qid":"76","text":"Submit","type":"control_button"}]);
   setTimeout(function() {
JotForm.paymentExtrasOnTheFly([null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,{"name":"heading","qid":"60","text":"SignUp","type":"control_head"},null,null,null,{"description":"","name":"typeA","qid":"64","subLabel":"","text":"Username","type":"control_textbox"},{"description":"","name":"name","qid":"65","text":"Name","type":"control_fullname"},{"description":"","name":"name66","qid":"66","text":"Name","type":"control_fullname"},{"description":"","name":"email","qid":"67","subLabel":"","text":"Email","type":"control_email"},{"description":"","name":"typeA68","qid":"68","text":"Type a question","type":"control_radio"},null,{"description":"","name":"typeA70","qid":"70","text":"Type a question","type":"control_radio"},null,null,{"description":"","name":"typeA73","qid":"73","subLabel":"","text":"Type a question","type":"control_textbox"},{"description":"","name":"typeA74","qid":"74","subLabel":"","text":"Type a question","type":"control_textbox"},{"description":"","name":"fileUpload","qid":"75","subLabel":"","text":"File Upload","type":"control_fileupload"},{"name":"submit","qid":"76","text":"Submit","type":"control_button"}]);}, 20);