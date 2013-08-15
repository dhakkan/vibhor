class Url < ActiveRecord::Base
	validate :url, :presence => true 
end
