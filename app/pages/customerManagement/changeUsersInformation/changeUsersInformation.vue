<template>
	<view>
		<form @submit="submitInformation">
			<view class='input-group'>
				<view class='input'>
					用户编号：<input name='userID' v-model="userID" placeholder="输入用户编号" />
				</view>
				<view class='input'>
					电话号码：<input name='telephone' v-model="telephone" placeholder="输入电话号码" />
				</view>
				<view class='input'>
					住址：<input name='address' v-model="address" placeholder="输入住址" />
				</view>
				<view class='input'>
					经度：<input name='longitude' v-model="longitude" placeholder="输入经度" />
				</view>
				<view class='input'>
					纬度：<input name='latitude' v-model="latitude" placeholder="输入纬度" />
				</view>
				<view class="input">紧急
					<switch @change="switchChange" :checked="checked" color='#F80004' class="switch"/>
				</view>
				<button @click="getusermessage">获取用户数据</button>
			</view>
			<view>
				<button form-type="submit" type="primary">提交</button>
			</view>
		</form>
	</view>
</template>

<script>
	var  r=/^1[3|4|5|8][0-9]\d{4,8}$/;
	export default{
		data(){
			return{
				userID:'',
				telephone:'',
				address:'',
				longitude:'',
				latitude:'',
				checked:false
			}
		},
		methods:{
			getusermessage:function(){
				uni.request({
					url:'http://182.92.239.229/getusermessage',
					data:{'id':this.userID},
					success: (res) => {
						console.log(res.data)
						this.telephone=res.data.phone;
						this.address=res.data.address;
						this.longitude=res.data.longitude;
						this.latitude=res.data.latitude;
						this.checked=res.data.emergency;
					}
				})
				
			},
			switchChange: function (e) {
				this.checked= e.target.value;
			        },
			submitInformation:function(e){
				
				if(e.detail.value.userID==''){
					uni.showToast({
						icon:'none',
						title:'未填写员工号'
					})
				}
				else if(!r.test(e.detail.value.telephone)){
					uni.showToast({
						icon:'none',
						title:'电话格式错误'
					})
				}
				else if(e.detail.value.address==''){
					uni.showToast({
						icon:'none',
						title:'未填写住址'
					})
				}
				else if(e.detail.value.longitude==''||e.detail.value.longitude>180||isNaN(e.detail.value.longitude)){
					uni.showToast({
						icon:'none',
						title:'经度格式不正确'
					})
				}
				else if(e.detail.value.latitude==''||e.detail.value.latitude>90||isNaN(e.detail.value.latitude)){
					uni.showToast({
						icon:'none',
						title:'纬度格式不正确'
					})
				}

				else{
					e.detail.value.emergency=this.checked;
					console.log('form发生了submit事件，携带数据为：' + JSON.stringify(e.detail.value))
					var formdata = e.detail.value;
					uni.request({
						url:'http://182.92.239.229/changeusermessage',
						data:e.detail.value,
						success: (res) => {
							console.log(res.data);
							if(res.data=='True'){
								uni.showToast({
									icon:'none',
									title:'修改成功'
								});
								setTimeout(function(){uni.navigateBack()},1000)
							}
							else{
								uni.showToast({
									icon:'none',
									title:'没有该用户'
								})
							}
						}
					})
					// uni.showModal({
					// 	content: '表单数据内容：' + JSON.stringify(formdata),
					// 	showCancel: false,
						
					// });
				}
			}
		}
	}
</script>

<style>
	.input{
		display: flex;
		margin: 30rpx;
		border-bottom: solid 1rpx #C8C7CC;
		
	}
	.picker{
		display: flex;
		margin: 30rpx;
		border-bottom: solid 1rpx #C8C7CC;
		
	}
	.switch{
		margin-right: 0rpx;
		margin-bottom: 0rpx;
	}
</style>

