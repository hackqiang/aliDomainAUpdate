# aliDomainAUpdate
##update the A record for Ali Domains

1. add your own accesskeys in `config/key.json`:

		{
	
	    	"access_key_id": "XXXXX",
	
	    	"access_key_secret": "XXXX"
	
		}

2. add your own domains in `config/domains.json`:

		[
	    	"hackqiang.org"
		]



3. `aliDomainAUpdate` used for ubuntu service:

		sudo cp aliDomainAUpdate /etc/init.d

		sudo update-rc.d aliDomainAUpdate defaults

		sudo service aliDomainAUpdate start

ref:
>
>https://develop.aliyun.com/sdk/python
>
>https://help.aliyun.com/document_detail/30003.html
>
>https://help.aliyun.com/document_detail/29739.html

>http://blog.csdn.net/bless2015/article/details/51284259
>
>http://blog.csdn.net/xp5xp6/article/details/53365696