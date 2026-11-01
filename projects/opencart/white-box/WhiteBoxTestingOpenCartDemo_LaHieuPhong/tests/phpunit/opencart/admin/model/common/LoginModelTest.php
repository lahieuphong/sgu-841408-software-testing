<?php

class AdminModelCommonLoginModelTest extends OpenCartTest {
	
	public function testCheckLogin() {

		$user_id = "";

		$data = array(
			'username' => 'admin',
			'email' => 'rmulmule@valethi.in',
		);

		$result = $this->db->query("SELECT * FROM " . DB_PREFIX . "user WHERE `username` = '".$data['username']."' AND `email` = '".$data['email']."'")->row;
		if(!empty($result)){
			$user_id = $result['user_id'];
		}

		$this->assertNotEmpty($user_id);
		$this->assertEquals(1,$user_id);
		
	}
}
